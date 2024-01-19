import pygame
from typing import Callable, List
from Abstract.Sprite import Sprite
import pygame
from pygame import Surface,Rect
from enum import Enum

class Static_UI(Sprite):
    def __init__(self, images: List[Surface], hitbox: Rect):
        super().__init__(images, hitbox)
    
    
    def update(self):
        #no update since it does not move
        pass

    def return_current_image(self) -> pygame.Surface:
        # do not have animations
        return self._image_arr[0]