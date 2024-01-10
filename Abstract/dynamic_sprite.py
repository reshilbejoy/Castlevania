from abc import abstractmethod
from abc import ABC
from Abstract.Sprite import Sprite
from CompletedSprites.Platform import Platform
from Utils.signals import DamageMessage,InventoryMessage
from typing import List
import pygame

class DynamicSprite(Sprite,ABC):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int, horizontal_force):
        super().__init__(images,hitbox)
        self._terminal_vel_x = terminal_vel_x
        self._terminal_vel_y = terminal_vel_y
        self._health = health
        self._horizontal_force = horizontal_force
        self._vertical_force = 0
        self.frictionForce = 0.2
        self.net_force = (abs(self.horizontalForce) - abs(self.frictionForce))
        self.starting_velocity_y = -15
        self.speed = 0
        self.left = False
        self.right = False
    
    
    @abstractmethod
    def handle_damage_interaction(interaction_msg:InventoryMessage)->None:
        #handle damage
        pass

    @abstractmethod
    def handle_inventory_interaction(interaction_msg:DamageMessage)->None:
        #handle inventory
        pass

    def apply_force(self,all_platforms:List[Platform])->None:
        #Use all platforms list to move the sprite hitbox according to x and y forces TODO
        if self.net_force > 0 and self._horizontal_force > 0:
            self.speeding_up()
            self._hitbox.left += self.speed
            self.left = False
            self.right = True
        elif self.net_force < 0 and self._horizontal_force < 0:
            self.speeding_up()
            self._hitbox.left -= self.speed
            self.left = True
            self.right = False

        if not self.speed <= 0 and self._horizontal_force == 0:
            self.slowing_down()
            if self.right:
                self._hitbox.left += self.speed
            else:
                self._hitbox.left -= self.speed
        
        if self.speed <= 0:
            self.left = False
            self.right = False
            self.net_force = 0
            self.speed = 0
        

    

    def change_force(self, x_force, y_force):
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


