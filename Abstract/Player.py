from Abstract.DynamicSprite import DynamicSprite
from typing import List
from abc import ABC, abstractmethod 
import pygame

class Player(DynamicSprite):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int):
        super.__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health)
    
    @abstractmethod
    def attack(self):
        pass
    
    def update(self):
        if not self.lifespan():
            del self
            
    def lifespan(self):
        return self._health>0
    
