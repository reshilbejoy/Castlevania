from abc import abstractmethod,ABC
from typing import Callable, List
import pygame
from Abstract.dynamic_sprite import DynamicSprite
from Abstract.Interaction import Interactable

class Enemy(DynamicSprite):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int, horizontal_force, create_interactable:[Callable[[Interactable],None]], remove_obj: Callable):
        self.remove_obj = remove_obj
        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health,horizontal_force,create_interactable,remove_obj)

    @abstractmethod
    def attack(self):
        pass

    def update(self):
        if self.lifespan():
            self.AI()
        else:
             self.remove_obj(self)


    def lifespan(self):
        return self._health > 0

    @abstractmethod
    def AI(self):
        pass
    
    @abstractmethod
    def init_obj() -> None:
        pass