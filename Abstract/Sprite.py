from typing import List
import pygame
from abc import ABC, abstractmethod
from background_engine import BackgroundEngine

class Sprite():
    def __init__(self,images:List[pygame.Surface],hitbox:pygame.Rect):
        self._image_arr:List[pygame.Surface] = images
        self._hitbox: pygame.Rect = hitbox
        self._screen:pygame.Rect = BackgroundEngine.get_current_image_frame(hitbox)
        self._global_coords = [self._hitbox.top, self._hitbox.left]
        

    @abstractmethod    
    def return_hitbox(self) -> pygame.Rect:
        return self._hitbox

    @abstractmethod
    def return_current_image(self) -> pygame.Surface:
        return self._image_arr[0]

    def draw(self, rect, surface):
        hitbox = self.get_hitbox()
        surface.blit(self.return_current_image(), (hitbox.left - rect.left, hitbox.top - rect.top))
        return surface

    def should_draw(self,player_hitbox:pygame.Rect) -> bool:
        # return wether or not to draw sprite based on player loc TODO
        #if self._screen.colliderect(player_hitbox):
            #return True
        return True
    
    def get_hitbox(self):
        return self._hitbox
    
    def should_update(self,player_hitbox:pygame.Rect)->bool:
        # return wether or not to call update function based on player loc TODO
        if (0 < player_hitbox.left < self._screen.width) and (0 < player_hitbox.top < self._screen.height):
            return True
        return False
        
    
    @abstractmethod
    def update(self):
        # update the coords or hitbox every frame IMPLEMENT IN DAUGHTER CLASSES
        pass