import pygame
from typing import List,Tuple
from abc import ABC
from Constants.window_constants import *

_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height

pygame.init()
window = pygame.display.set_mode((length, height + score_box_height))
pygame.display.set_caption("Castlevania")

_background_arr:List[pygame.Surface] = [pygame.transform.scale(pygame.image.load('Assets//Background/Level_1/1.png'), (background_length, height_ratio * size)),
                                        pygame.transform.scale(pygame.image.load('Assets//Background/Level_1/2.png'), (background_length, height_ratio * size)),
                                        pygame.transform.scale(pygame.image.load('Assets//Background/Level_1/3.png'), (background_length, height_ratio * size)),
                                        pygame.transform.scale(pygame.image.load('Assets//Background/Level_1/1.png'), (background_length, height_ratio * size))]
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height


class BackgroundEngine(ABC):
    
    @staticmethod
    def get_current_image(player_global_hitbox:pygame.Rect, level): #-> pygame.Rect, pygame.Surface:

        # a surface which is the same dimensions
        image_rect = BackgroundEngine.get_current_image_frame(player_global_hitbox, level)
        surface = pygame.Surface((image_rect.width, image_rect.height))
        surface.blit(_background_arr[level], (-image_rect.left, 0))

        return image_rect, surface
    
    @staticmethod
    def get_window():
        return window

    @staticmethod
    def get_current_image_frame(player_global_hitbox:pygame.Rect, level)-> pygame.rect:
        # the rectangle around the player
        if level == 3:
            backgroundLength = 1590
        else:
            backgroundLength = background_length
        window_rect = pygame.Rect(0, 0, length, height)
        if (player_global_hitbox.left < (length / 2)):
            window_rect.left = 0
        elif player_global_hitbox.left > (backgroundLength - (length / 2)):
            window_rect.left = (backgroundLength - (length))
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
        _timer.tick(30)
