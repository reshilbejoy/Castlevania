from Abstract.dynamic_sprite import DynamicSprite
from Abstract.Enemy import Enemy
from typing import Callable, List
from abc import ABC, abstractmethod 
import pygame
from Abstract.Interaction import Interactable
from CompletedSprites.Interactables.HarmingHitbox import HarmingHitbox
from CompletedSprites.Interactables.CandyCane import CandyCane

from background_engine import BackgroundEngine


from Utils.signals import DamageMessage, InventoryMessage, TargetType

class Skeleton(Enemy):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox: pygame.Rect, health:int, horizontal_force, create_interactable:[Callable[[Interactable],None]], remove_interctable: Callable, get_player_pose: Callable, level):

        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health, horizontal_force,create_interactable,remove_interctable) 
        self.alignment = 0
        self.walkLeft = [pygame.transform.scale(pygame.image.load('Assets/Enemies/Ghost_walk/1.png'),(hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Enemies/Ghost_walk/2.png'),(hitbox.width, hitbox.height)),]
        self.walkRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Enemies/Ghost_walk/1.png'),True,False),(hitbox.width, hitbox.height)),
                        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Enemies/Ghost_walk/2.png'),True,False),(hitbox.width, hitbox.height)),]
        self.get_player_pose = get_player_pose
        self.invincible = False
        self.invince_time_ms = 200
        self.last_invince_timestep = 0
        self.movement_time_ms = 2000
        if level == 3:
            self.movement_time_ms = 500
        self.sp = 0
        self.walkIndex = 0
        self._score = 500
        self.flag = False
        

    def init_obj(self):
        self.create_obj(HarmingHitbox (pygame.Rect(50, 200, 100, 30), self.get_pose_supplier(),TargetType.PLAYER,self.remove_obj,5))


    def attack(self):
        pass
        #   self.create_obj(HarmingHitbox(pygame.Rect(50, 200, 100, 30), self.get_pose_supplier(),TargetType.PLAYER,self.remove_obj,5))

    def return_current_image(self) -> pygame.Surface:
        if self._health > 0:
            self.walkIndex+=1
            if self.sp == 1:
                return self.walkRight[self.walkIndex % 2]
            elif self.sp == 0:
                return self.walkLeft[self.walkIndex % 2]
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
        if self.sp == 0:
            self.change_force(-0.25, 0)
            if (BackgroundEngine.get_current_time() - self.current_time) > self.movement_time_ms:
                self.current_time = BackgroundEngine.get_current_time()
                self.sp = 1  
        elif self.sp == 1:
            self.change_force(0.25, 0)
            if (BackgroundEngine.get_current_time() - self.current_time) > self.movement_time_ms: 
                self.current_time = BackgroundEngine.get_current_time()
                self.sp = 0 
        if (BackgroundEngine.get_current_time() // 2500) % 2 == 0:
            if not self.flag:
                self.flag = True
                self.create_obj(CandyCane(pygame.Rect(50, 200, 50, 30), self.get_pose_supplier(),TargetType.PLAYER,self.remove_obj,-1))
                self.create_obj(CandyCane(pygame.Rect(50, 200, 50, 30), self.get_pose_supplier(),TargetType.PLAYER,self.remove_obj,1))
        else:
            self.flag = False