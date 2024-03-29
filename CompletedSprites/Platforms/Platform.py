from typing import List
import pygame
from Abstract.Sprite import Sprite
import pygame
from pygame import Surface,Rect
from enum import Enum

class PlatformType(Enum):
    NORMAL_PLATFORM = 1,
    STAIRWAY = 2

class Platform(Sprite):
    def __init__(self, images: List[Surface], hitbox: Rect, platform: PlatformType):
        self._platform = platform # How to convert images to surfaces TODO
        super().__init__(images, hitbox)
    
    def get_platform_type(self) -> PlatformType:
        return self._platform
    
    def update(self):
        #has no update since it does not move
        pass

    def return_current_image(self) -> pygame.Surface:
        #returns first image bec platforms do not have animations
        return self._image_arr[0]
        
    

