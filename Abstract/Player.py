from Abstract.dynamic_sprite import DynamicSprite
from typing import Callable, List
from abc import ABC, abstractmethod 
import pygame
from Abstract.Interaction import Interactable
from background_engine import BackgroundEngine

from Utils.signals import DamageMessage, InventoryMessage

class Player(DynamicSprite):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface],
     hitbox: pygame.Rect, health:int, horizontal_force, create_obj:Callable,remove_obj:Callable):
    
     self._hit = False
     self._dead = False
     self.timestamp = 0

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
        if not self._dead:
            return True
        else:
            return False

    def return_current_image(self) -> pygame.Surface:
        pass

    def inside_door(self, door):
        if (self.hitbox.colliderect(door.get_hitbox())):
            return True
        return False
    
    def handle_damage_interaction(interaction_msg: InventoryMessage) -> None:
        return super().handle_damage_interaction()
    
    def handle_inventory_interaction(interaction_msg: DamageMessage) -> None:
        return super().handle_inventory_interaction()

    def draw(self, rect, surface):
        hitbox = self.get_hitbox()
        if self._health <= 0:
            if BackgroundEngine.get_current_time() - self.timestamp <= 2000:
                surface.blit(self.return_current_image(), (hitbox.left - rect.left, hitbox.top - rect.top + 30))
            else:
                surface.blit(self.return_current_image(), (hitbox.left - rect.left, hitbox.top - rect.top + 50))
        else:
            surface.blit(self.return_current_image(), (hitbox.left - rect.left, hitbox.top - rect.top))
        #pygame.draw.rect(surface, (200, 90, 90), (hitbox.left - rect.left,hitbox.top - rect.top, hitbox.width, hitbox.height), 2)
        return surface
            
        
       # return super().return_current_image()d
    
