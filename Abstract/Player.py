from Abstract.dynamic_sprite import DynamicSprite
from typing import List
from abc import ABC, abstractmethod 
import pygame

from Utils.signals import DamageMessage, InventoryMessage

class Player(DynamicSprite):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox: pygame.Rect, health:int, horizontal_force):

        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health, horizontal_force)
    
    @abstractmethod
    def attack(self):
        pass
    
    def update(self):
        if not self.lifespan():
            del self
            
    def lifespan(self):
        return self._health>0

    def return_current_image(self) -> pygame.Surface:
        pass
    
    def handle_damage_interaction(interaction_msg: InventoryMessage) -> None:
        return super().handle_damage_interaction()
    def handle_inventory_interaction(interaction_msg: DamageMessage) -> None:
        return super().handle_inventory_interaction()
            
        
       # return super().return_current_image()d
    
