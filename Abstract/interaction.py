from enum import Enum
from typing import List
import pygame
from abc import abstractmethod,ABC
from Abstract.dynamic_sprite import DynamicSprite
from Utils.signals import DamageMessage,InventoryMessage
from Abstract.sprite import Sprite

from enum import Enum

    
class Interactable(Sprite,ABC):
    def __init__(self, images: List[pygame.Surface], hitbox: List[pygame.Rect], damage: int):
        self._damage = damage
        super().__init__(images, hitbox)
    
    @abstractmethod
    def _movement(self):
        pass
    
    @abstractmethod
    def life_span(self):
        pass
    
    def damage_interaction(self,obj:DynamicSprite,msg:DamageMessage):
        obj.handle_damage_interaction(msg)
    
    def inventory_interaction(self,obj:DynamicSprite,msg:InventoryMessage):
        obj.handle_inventory_interaction(msg)

    def update(self):
        return super().update()