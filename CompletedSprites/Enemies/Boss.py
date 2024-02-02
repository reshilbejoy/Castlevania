import math
import numpy as np
from Abstract.dynamic_sprite import DynamicSprite
from Abstract.Enemy import Enemy
from typing import Callable, List
from abc import ABC, abstractmethod 
import pygame
from Abstract.Interaction import Interactable
from CompletedSprites.Interactables.Candle import Candle
from CompletedSprites.Interactables.HarmingHitbox import HarmingHitbox
from background_engine import BackgroundEngine
from CompletedSprites.Platforms.Platform import Platform


from Utils.signals import DamageMessage, InventoryMessage, TargetType

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
        
def sign(num):
    return -1 if num < 0 else 1
def bDist(tuple1,tuple2):
    return math.fabs(math.sqrt((tuple2[0] - tuple1[0])**2 + (tuple2[1]-tuple1[1])**2))
class PIDController():
    def __init__(self,p,d) -> None:
        self.p = p
        self.d = d
        self.last_error = 0
        self.last_error_ts = BackgroundEngine.get_current_time()
    
    def calculate(self,m,sp):
        error = sp-m
        curTime = BackgroundEngine.get_current_time()
        out = error*self.p + (error-self.last_error)/(curTime-self.last_error_ts)*self.d
        # out = error*self.p + (error-self.last_error)*self.d

        self.last_error_ts = curTime
        self.last_error = error
        return out
    
class Boss(Enemy):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox: pygame.Rect, health:int, horizontal_force, create_interactable:[Callable[[Interactable],None]], remove_interctable: Callable, get_player_pose: Callable):

        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health, horizontal_force,create_interactable,remove_interctable) 
        self.alignment = 0
        self.walkLeft = [pygame.transform.scale(pygame.image.load('Assets/Enemies/Ghoul_walk/1.png'),(hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Enemies/Ghoul_walk/2.png'),(hitbox.width, hitbox.height)),]
        self.walkRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Enemies/Ghoul_walk/1.png'),True,False),(hitbox.width, hitbox.height)),
                        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Enemies/Ghoul_walk/2.png'),True,False),(hitbox.width, hitbox.height)),]
        self.pose_supplier:Callable = get_player_pose
        self.invincible = False
        self.invince_time_ms = 200
        self.last_invince_timestep = 0
        self.movement_time_ms = 1000
        self.sp = 0
        self.walkIndex = 0
        self._score = 200
        self.a_star_nodes = []
        self.last_astar_exec = []
        self.movement_pid_controller = PIDController(0.001,0.0001)
        self.current_player_pose = 0
        self.path_replanning_thresh_ms = 200


    def init_obj(self):
        self.create_obj(HarmingHitbox(pygame.Rect(50, 200, 100, 100), self.get_pose_supplier(),TargetType.PLAYER,self.remove_obj,5))

    def attack(self):
        pass

    def populate_node_map(self,allPlats:[Platform]):
        self.a_star_nodes = []
        for plat in [i.get_hitbox() for i in allPlats]:
            print("__________________________________________________")
            for x in np.arange(plat.midleft[0]+2,plat.midright[0],10):
                # print(f"astar plat center {plat.centery}")
                print(f"astar plat top {[x,plat.top]}")

                self.a_star_nodes.append([x,plat.top])
                # print(f"a star node{(x,plat.top)}")
                # self.create_obj(Candle([pygame.transform.scale((pygame.image.load('Assets/Interactables/BigCandle/1.png')), (60, 20)), 
                #             pygame.transform.scale((pygame.image.load('Assets/Interactables/BigCandle/2.png')), (60, 20))],pygame.Rect(x,plat.top,50,50),self.create_obj,self.remove_obj))


    def get_best_path(self):
        closest_node_to_enemy = []
        closest_e_node_dist = 100000000000
        
        closest_node_to_player = []
        closest_p_node_dist = 100000000000

        for i in self.a_star_nodes:

            enemy_node_dist = math.dist(self.get_hitbox().midbottom,i)

            if enemy_node_dist<closest_e_node_dist:
                closest_node_to_enemy = i
                closest_e_node_dist = enemy_node_dist

        for i in self.a_star_nodes:

            player_node_dist = math.dist(self.pose_supplier()[0].midbottom,i)

            if player_node_dist<closest_p_node_dist:
                closest_node_to_player = i
                closest_p_node_dist = player_node_dist
        
        
        # print(f"closest player node dist: {player_node_dist}")
        # print(f"closest enemy node dist: {enemy_node_dist}")
        # print(f"closest node to player:{closest_node_to_player}")
        # print(f"closest node to enemy:{closest_node_to_enemy}")
        # print(f"player pose: {self.current_player_pose}")
        # print(f"enemy pose: {self.get_hitbox().midbottom}")

        astar_out = self.astar(closest_node_to_enemy,closest_node_to_player)
        self.last_astar_exec = [astar_out,0,BackgroundEngine.get_current_time()]
        print(f"Last astar exec: {astar_out}")
        for i in astar_out:
            print(f"Last astar exec: {astar_out}")
            # self.create_obj(Candle([pygame.transform.scale((pygame.image.load('Assets/Interactables/BigCandle/1.png')), (60, 20)), 
            #         pygame.transform.scale((pygame.image.load('Assets/Interactables/BigCandle/2.png')), (60, 20))],pygame.Rect(i[0],i[1],50,50),self.create_obj,self.remove_obj))

        # print(astar_out)
        return astar_out

    def getPossibleCoords(self,curNode:Node):
        posNodes = []
        for posNode in self.a_star_nodes:
            if (math.dist(curNode.position,posNode)<200):
                posNodes.append(posNode)

        if len(posNodes) == 0:
            print("no possible paths from here")
        posNodes.remove(curNode.position)

        return posNodes
    
    def astar(self, start, end):

        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0
        open_list = []
        closed_list = []

        open_list.append(start_node)

        while len(open_list) > 0:

            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]

            children = []
            # print(f'currentNode {end}')
            for new_position in self.getPossibleCoords(current_node):
                new_node = Node(current_node, new_position)
                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)

    def return_current_image(self) -> pygame.Surface:
        if self._health > 0:
            self.walkIndex+=0.05
            if self.sp == 1:
                return self.walkRight[int(self.walkIndex) % 2]
            elif self.sp == 0:
                return self.walkLeft[int(self.walkIndex) % 2]
        if BackgroundEngine.get_current_time() - self.timestamp <= 300:
            return self._death[0]
        elif BackgroundEngine.get_current_time() - self.timestamp <= 900:
            return self._death[1]
        else:
            if BackgroundEngine.get_current_time() - self.timestamp > 1200:
                self._dead = True
            return self._death[2]
        
    def handle_damage_interaction(self,interaction_msg: DamageMessage) -> None:
            if interaction_msg.target == (TargetType.ENEMY or TargetType.ALL_SPRITES):
                if interaction_msg.damage > 0:
                    if((BackgroundEngine.get_current_time()-self.last_invince_timestep) > self.invince_time_ms):
                        self.invincible = True
                        self.last_invince_timestep = BackgroundEngine.get_current_time()
                        self._health -= interaction_msg.damage
                        self._hit = True
                else:
                    self._health -=interaction_msg.damage
                    self._hit = True
                self._hit_time = BackgroundEngine.get_current_time()
            if self._health <= 0 and self.timestamp == 0:
                self.timestamp = BackgroundEngine.get_current_time()

    def handle_inventory_interaction(self,interaction_msg: InventoryMessage) -> None:
        pass

    def AI(self):
        try:
            # print(f" pose {self.current_player_pose}")
            
            if self.last_astar_exec[1] <= len(self.last_astar_exec[0])-1 and (BackgroundEngine.get_current_time()-self.last_astar_exec[2])<self.path_replanning_thresh_ms:
                # print("execution")

                x_error = self.last_astar_exec[0][self.last_astar_exec[1]][0] - self.get_hitbox().centerx 
                y_error = self.last_astar_exec[0][self.last_astar_exec[1]][1] - self.get_hitbox().bottom 
                error = math.dist((self.get_hitbox().centerx,self.get_hitbox().bottom),self.last_astar_exec[0][self.last_astar_exec[1]])
                print(f"desired pose is {self.last_astar_exec[0][self.last_astar_exec[1]][0]}")
                print(f"current pose is {self.get_hitbox().centerx }")

                print(f"error is {x_error}")

                if (math.fabs(x_error)+ math.fabs(y_error))>25:
                    pidOut = self.movement_pid_controller.calculate(self.get_hitbox().centerx, self.last_astar_exec[0][self.last_astar_exec[1]][0])
                    print(f"pidOut {pidOut}")
                    self.change_force(pidOut+sign(pidOut)*0.2,0)
                    if (self.get_hitbox().midbottom[1] - self.last_astar_exec[0][self.last_astar_exec[1]][1]) > 3:
                        self.jump()
                else:
                    self.last_astar_exec = [self.last_astar_exec[0],self.last_astar_exec[1]+1,self.last_astar_exec[2]]

            else:
                # self.populate_node_map()
                self.get_best_path()
            pass
        except Exception as e:
            print(e)
        


    def update(self):
        if self.lifespan():
            self.AI()
        else:
             self.remove_obj(self)
    

            