import pygame
from typing import List,Tuple
from abc import ABC
from Constants.window_constants import length, height

_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height

pygame.init()
size = 35
height_ratio = 14
length_ratio = 22
window_size = (600,500)
window = pygame.display.set_mode((length_ratio * size, height_ratio * size))
pygame.display.set_caption("Castlevania")
<<<<<<< HEAD
background_length = 1200
_normal_background = pygame.transform.scale(pygame.image.load('Assets/Background-easy.png'), (background_length, height_ratio * size))
=======
_normal_background = pygame.transform.scale(pygame.image.load('Assets/Background-easy.png'), (1200, height_ratio*size))
>>>>>>> adding movement
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
        surface.blit(_normal_background, (0, 0))

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
            window_rect.left = (background_length - (length / 2))
        else:
            window_rect.left = player_global_hitbox.left - (length / 2)

        return window_rect


    @staticmethod
    def get_current_update_frame(player_hitbox:pygame.Rect)-> pygame.Rect:
        #Return a Rect with the frame objects should update in TODO
        pass

    @staticmethod
    def get_current_time()-> float:
        _timer.get_time()

    @staticmethod
    def tick_timer()-> float:
        pygame.display.update()
        _timer.tick()
