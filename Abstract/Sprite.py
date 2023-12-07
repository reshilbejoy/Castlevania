from typing import List
import pygame
from abc import ABC, abstractmethod
from background_engine import BackgroundEngine

class Sprite():
    def __init__(self,images:List[pygame.Surface],hitbox:List[pygame.Rect]):
        self._image_arr:List[pygame.Surface] = images
        self._hitbox_arr:List[pygame.Rect] = hitbox
        self._screen:pygame.Surface = BackgroundEngine.get_current_image()
        
    def return_hitbox(self) -> pygame.Rect:
        # return a compound hitbox of the sprite from rect_arr TODO
        pass

    @abstractmethod
    def return_current_image(self) -> pygame.Surface:
        # return an image based off the animation timing IMPLEMENT IN DAUGHTER CLASSES
        pass

    def draw(self):
        self._screen.blit(self.return_current_image(), self.return_hitbox())

    def should_draw(self,player_hitbox:pygame.Rect) -> bool:
        # return wether or not to draw sprite based on player loc TODO
        player_x = player_hitbox.left
        player_y = player_hitbox.top
        pass
    
    def should_update(self,player_hitbox:pygame.Rect)->bool:
        # return wether or not to call update function based on player loc TODO
        pass
    
    @abstractmethod
    def update(self):
        # update the coords or hitbox every frame IMPLEMENT IN DAUGHTER CLASSES
        pass