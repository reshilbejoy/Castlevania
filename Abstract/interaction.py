from enum import Enum
from typing import List
import pygame
from abc import abstractmethod,ABC
from dynamic_sprite import DyanmicSprite
from sprite import Sprite

from enum import Enum

class Item(Enum):
    WHIP = 1
    DAGGER = 2


class DamageMessage():
    def __init__(self, damage:int) -> None:
        self._damage = damage

    def get_damage(self):   
        return self._damage
    
class InventoryMessage():
    def __init__(self, equip:Item) -> None:
        self._item = equip

    def get_item(self):
        return self._item
    
class Interactable(Sprite,ABC):
    def __init__(self, images: List[pygame.Surface], hitbox: List[pygame.Rect], damage: int, attackable:DyanmicSprite):
        self._damage = damage
        super().__init__(images, hitbox)
    
    @abstractmethod
    def _movement(self):
        pass
    
    @abstractmethod
    def life_span(self):
        pass
    
    def damage_interaction(self,obj:DyanmicSprite,msg:DamageMessage):
        obj.handle_damage_interaction(msg)
    
    def inventory_interaction(self,obj:DyanmicSprite,msg:InventoryMessage):
        obj.handle_inventory_interaction(msg)

    def update(self):
        return super().update()