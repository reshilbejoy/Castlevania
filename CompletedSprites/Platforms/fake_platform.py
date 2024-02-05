from typing import List
import pygame
from Abstract.Sprite import Sprite
import pygame
from pygame import Surface,Rect
from enum import Enum

class PlatformType(Enum):
    NORMAL_PLATFORM = 1,
    STAIRWAY = 2

class FakePlatform(Platform):
    def __init__(self, images: List[Surface], hitbox: Rect, platform: PlatformType):
        super().__init__9self, images: List[Surface], hitbox: Rect, platform: PlatformType): 
    
    def byebye(self):
        del(self)