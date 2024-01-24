from typing import List
import pygame
from Abstract.Sprite import Sprite
import pygame
from pygame import Surface,Rect
from enum import Enum

class Door(Sprite):
    def __init__(self, images: List[Surface], hitbox: Rect):
        super().__init__(images, hitbox)
    
    def update(self):
        #Platform has no update since it does not move
        pass

    def return_current_image(self) -> pygame.Surface:
        #returns first image bec platforms do not have animations
        return self._image_arr[0]

    def get_hitbox(self):
        return self._hitbox
    
        