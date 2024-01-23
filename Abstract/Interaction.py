from typing import Callable, List
import pygame
from abc import abstractmethod,ABC
from Abstract.Sprite import Sprite

    
class Interactable(Sprite,ABC):
    def __init__(self, images: List[pygame.Surface], hitbox: List[pygame.Rect], damage: int,remove_obj:Callable):
        self.damage = damage
        self.remove_obj = remove_obj
        super().__init__(images, hitbox)
    
    @abstractmethod
    def _movement(self):
        pass

    @abstractmethod
    def life_span(self):
        pass

    @abstractmethod
    def get_damage_message(self):
        #return damage_message based on target types and damage output
        pass     

    @abstractmethod
    def get_inventory_message(self):
        #return inventory_message based on target types and recorded item
        pass   

    def update(self):
        if self.life_span():
            self._movement()
        else:
            self.remove_obj(self)