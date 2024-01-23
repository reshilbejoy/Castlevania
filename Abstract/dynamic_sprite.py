from abc import abstractmethod
from abc import ABC
from Abstract.Sprite import Sprite
from CompletedSprites.Platforms.Platform import Platform
from Abstract.Interaction import Interactable
from Utils.signals import DamageMessage,InventoryMessage
from typing import Callable, List
import pygame
from Constants.window_constants import background_length
import time

class DynamicSprite(Sprite,ABC):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], 
                 health:int, horizontal_force,create_obj:Callable,remove_obj:Callable):
        super().__init__(images,hitbox)
        self.remove_obj:Callable = remove_obj
        self.create_obj:Callable = create_obj
        self._terminal_vel_x = terminal_vel_x
        self._terminal_vel_y = terminal_vel_y
        self._health = health
        self._horizontal_force = horizontal_force
        self._vertical_force = 0
        self.frictionForce = 0.2
        self.net_force = (abs(self.horizontalForce) - abs(self.frictionForce))
        self.speed = 0
        #self.left = False
        #self.right = False
        self.current_velocity = 0 # y velocity
        self.collision_detection = False
        self.isJumping = False
        self.isFalling = False
        self.gravity = 0.5
        self.collision_left = False
        self.collision_right = False
        self.direction = 0 # 0 standing still, 1 right, -1 left
    
    @abstractmethod
    def handle_damage_interaction(interaction_msg:InventoryMessage)->bool:
        #handle damage
        #while
        pass

    @abstractmethod
    def handle_inventory_interaction(interaction_msg:DamageMessage)->None:
        #handle inventory
        pass

    def apply_force(self,all_platforms:List[Platform])->None:
        #Use all platforms list to move the sprite hitbox according to x and y forces TODO

        # vertical apply force
        self.collision_detection = False
        self.collision_right = False
        self.collision_left = False
        self.canMove = True

        for platform in all_platforms:
            self.platform_collision_detection(platform)

        self.horizontal_movement()

        if self.speed <= 0 and self._horizontal_force == 0:
            self.direction = 0
            self.net_force = 0
            self.speed = 0

        if not self.collision_detection: # collision_detection is true if there is a normal force
            self.current_velocity += self.gravity
            self._hitbox.top += self.current_velocity
            if self.current_velocity > 0:
                self.isFalling = True
    
    def horizontal_movement(self):
        if self.net_force > 0 and self._horizontal_force > 0 and self._hitbox.left <= background_length - self._hitbox.width: # and not self.collision_right:
            if not self.collision_right:
                self.speeding_up()
                self._hitbox.left += self.speed
            self.direction = 1
        elif self.net_force < 0 and self._horizontal_force < 0 and self._hitbox.left >= 0: #and not self.collision_left:
            if not self.collision_left:
                self.speeding_up()
                self._hitbox.left -= self.speed
            self.direction = -1

        if not self.speed <= 0 and self._horizontal_force == 0:
            if self._hitbox.left <= 0 or self._hitbox.left >= background_length - self._hitbox.width:
                self.speed = 0
            else:
                self.slowing_down()
                if self.direction > 0:
                    self._hitbox.left += self.speed
                else:
                    self._hitbox.left -= self.speed

    def platform_collision_detection(self, platform):
        # collision in the x direction
        if platform._hitbox.colliderect(self._hitbox.left + (self._terminal_vel_x * self.direction), self._hitbox.top - 1, self._hitbox.width, self._hitbox.height):
            self.speed = 0
            if self.direction > 0:
                self.collision_right = True
                self._hitbox.right = platform._hitbox.left
            elif self.direction < 0:
                self.collision_left = True
                self._hitbox.left = platform._hitbox.right
        
        # collision in the y direction
        if platform._hitbox.colliderect(self._hitbox.left, self._hitbox.top + self.current_velocity, self._hitbox.width, self._hitbox.height):
            if self.current_velocity < 0:
                self.current_velocity = 0
                self._hitbox.top = platform._hitbox.bottom + 1
            elif self.current_velocity >= 0:
                self.current_velocity = 0
                self.isJumping = False
                self.isFalling = False
                self.collision_detection = True
                self._hitbox.bottom = platform._hitbox.top + 1
            
    def change_force(self, x_force, y_force):
        if not (self.isJumping or self.isFalling) or x_force == 0:
            self._horizontal_force = x_force
            self._verticalForce = y_force
            self.net_force = (abs(self._horizontal_force) - abs(self.frictionForce))
            if self._horizontal_force < 0:
                self.net_force *= -1    

    def speeding_up(self):
        if self.speed < self._terminal_vel_x:
            speed_val = self.speed + abs(self.net_force)
            self.speed = round(speed_val, 2)
    
    def slowing_down(self):
        if self.speed > 0:
            speed_val = self.speed - abs(self.frictionForce)
            self.speed = round(speed_val, 2)

    def jump(self):
        self.isJumping = True
        self.collision_detection = False
        self.current_velocity = -self._terminal_vel_y
        self._hitbox.top += self.current_velocity

    def get_pose_supplier(self):
        return lambda : (self.get_hitbox(),self.direction)
        


