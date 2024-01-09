from abc import abstractmethod
from abc import ABC
from Abstract.Sprite import Sprite
from CompletedSprites.Platform import Platform
from Utils.signals import DamageMessage,InventoryMessage
from typing import List
import pygame

class DynamicSprite(Sprite,ABC):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int):
        super().__init__(images,hitbox)
        self._terminal_vel_x = terminal_vel_x
        self._terminal_vel_y = terminal_vel_y
        self._health = health
    
    
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
        if self.net_force > 0:
            self.speeding_up()
            self._global_coords[0] = self._global_coords[0] + self.speed
                
        elif self.net_force < 0:
            self.speeding_up()
            self._global_coords[0] = self._global_coords[0] - self.speed
        
        else:
            self.speed = 0

                
        if  not self.speed <= 0:
            self.net_force = self.frictionForce
            new_speed = self.speed - self.net_force
            self.speed = round(new_speed, 2)
    

    def change_force(self, x_force, y_force):
        self.horizontalForce = x_force
        self.verticalForce = y_force
        self.net_force = (abs(self.horizontalForce) - abs(self.frictionForce))

    def speeding_up(self):
        if self.speed < self._terminal_vel_x:
            speed_val = self.speed + self.net_force
            self.speed = round(speed_val, 2)


