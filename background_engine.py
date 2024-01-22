import pygame
from typing import List,Tuple
from abc import ABC
from Constants.window_constants import *

_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height

pygame.init()
window = pygame.display.set_mode((length, height + 150))
pygame.display.set_caption("Castlevania")

_normal_background = pygame.transform.scale(pygame.image.load('Assets//Background/Level_1/1.png'), (background_length, height_ratio * size))
_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height


class BackgroundEngine(ABC):
    
    @staticmethod
    def get_current_image(player_global_hitbox:pygame.Rect): #-> pygame.Rect, pygame.Surface:

        # a surface which is the same dimensions
        image_rect = BackgroundEngine.get_current_image_frame(player_global_hitbox)
        surface = pygame.Surface((image_rect.width, image_rect.height))
        surface.blit(_normal_background, (-image_rect.left, 0))

        return image_rect, surface
    
    @staticmethod
    def get_window():
        return window

    @staticmethod
    def get_current_image_frame(player_global_hitbox:pygame.Rect)-> pygame.Rect:
        # the rectangle around the player
        window_rect = pygame.Rect(0, 0, length, height)
        if (player_global_hitbox.left < (length / 2)):
            window_rect.left = 0
        elif player_global_hitbox.left > (background_length - (length / 2)):
            window_rect.left = (background_length - (length))
        else:
            window_rect.left = player_global_hitbox.left - (length / 2)

        return window_rect

    @staticmethod
    def get_current_update_frame(player_hitbox:pygame.Rect)-> pygame.Rect:
        #Return a Rect with the frame objects should update in TODO
        pass

    @staticmethod
    def get_current_time()-> float:
        return pygame.time.get_ticks()

    @staticmethod
    def tick_timer()-> float:
        pygame.display.update()
        _timer.tick(60)
