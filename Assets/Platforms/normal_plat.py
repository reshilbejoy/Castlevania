from typing import List
import pygame
from Abstract.sprite import Sprite
class NormalPlat(Sprite):
    def __init__(self, images: List[pygame.Surface], hitbox: List[pygame.Rect]):
        super().__init__(images, hitbox)
    
    def return_hitbox(self) -> pygame.Rect:
        return self._hitbox_arr[0]

    def return_current_image(self) -> pygame.Surface:
        # return an image based off the animation timing IMPLEMENT IN DAUGHTER CLASSES
        return self._image_arr[0]

    def update():
        None
