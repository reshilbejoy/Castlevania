from typing import List
import pygame
from Abstract.Sprite import Sprite
import pygame
from pygame import Surface,Rect
from enum import Enum

class Door(Sprite):
    def __init__(self, images: List[Surface], hitbox: Rect, req: int, font):
        self.req = req
        self.font = pygame.font.Font('Assets/Background/controls.ttf', 10)
        super().__init__(images, hitbox)
    
    def update(self):
        #Platform has no update since it does not move
        pass

    def return_current_image(self) -> pygame.Surface:
        #returns first image bec platforms do not have animations
        return self._image_arr[0]

    def get_hitbox(self):
        return self.hitbox

    def draw(self, rect, surface):
        hitbox = self.get_hitbox()
        text = self.font.render(str(self.req), 1, (255, 255, 255))
        text_rect = text.get_rect(center=(hitbox.left - rect.left + int(hitbox.width / 2), hitbox.top - rect.top + (int(hitbox.height / 2))))
        surface.blit(self.return_current_image(), (hitbox.left - rect.left, hitbox.top - rect.top))
        surface.blit(text, text_rect)
        return surface

    
        