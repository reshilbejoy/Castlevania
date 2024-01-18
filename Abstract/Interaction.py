from typing import List
import pygame
from abc import abstractmethod,ABC
from Abstract.Sprite import Sprite

    
class Interactable(Sprite,ABC):
    def __init__(self, images: List[pygame.Surface], hitbox: List[pygame.Rect], damage: int):
        self.damage = damage

        super().__init__(images, hitbox)
    
    @abstractmethod
    def _movement(self):
        pass
    
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
        return super().update()