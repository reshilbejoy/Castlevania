from abc import abstractmethod
from abc import ABC
from sprite import Sprite
from CompletedSprites.platform import Platform
from interaction import DamageMessage,InventoryMessage
from typing import List
import pygame

class DyanmicSprite(Sprite,ABC):
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

    def apply_force(self,x_force,y_force, all_platforms:List[Platform])->None:
        #Use all platforms list to move the sprite hitbox according to x and y forces TODO
        pass

