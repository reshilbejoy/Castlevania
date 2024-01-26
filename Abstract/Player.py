from Abstract.dynamic_sprite import DynamicSprite
from typing import Callable, List
from abc import ABC, abstractmethod 
import pygame
from Abstract.Interaction import Interactable

from Utils.signals import DamageMessage, InventoryMessage

class Player(DynamicSprite):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface],
     hitbox: pygame.Rect, health:int, horizontal_force, create_obj:Callable,remove_obj:Callable):

        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health, horizontal_force,create_obj,remove_obj)
    
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def init_obj(self) -> None:
        pass

    def update(self):
        if not self.lifespan():
            self.remove_obj(self)
            
    def lifespan(self):
        return self._health>0

    def return_current_image(self) -> pygame.Surface:
        pass

    def inside_door(self, door):
        if (self._hitbox.colliderect(door.get_hitbox())):
            return True
        return False
    
    def handle_damage_interaction(interaction_msg: InventoryMessage) -> None:
        return super().handle_damage_interaction()
    
    def handle_inventory_interaction(interaction_msg: DamageMessage) -> None:
        return super().handle_inventory_interaction()
            
        
       # return super().return_current_image()d
    
