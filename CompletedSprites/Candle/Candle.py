from typing import List
import pygame
from Abstract.Sprite import Sprite
import pygame
from pygame import Surface,Rect
from enum import Enum

class Candle(Sprite):
    def __init__(self, images: List[Surface], hitbox: Rect):
        super().__init__(images, hitbox)
        self.index = 0
    
    def update(self):
        #Platform has no update since it does not move
        pass

    def return_current_image(self) -> pygame.Surface:
        self.index += 0.05
        #returns first image bec platforms do not have animations
        return self._image_arr[int(self.index) % 2]

    def get_hitbox(self):
        return self._hitbox
    
        