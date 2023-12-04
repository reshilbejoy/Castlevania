from abc import abstractmethod,ABC
from typing import List
import pygame
from DynamicSprite import DyanmicSprite


class Enemy(DyanmicSprite,ABC):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int):
        super.__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health)
    
    @abstractmethod
    def attack(self):
        pass

    def update(self):
        if self.lifespan():
            self.AI()
        else:
            del self

    @abstractmethod       
    def lifespan(self):
        pass
    
    @abstractmethod
    def AI(self):
        pass