import pygame
from typing import List,Tuple
from abc import ABC

_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height

pygame.init()
size = 35
height_ratio = 14
length_ratio = 22
window_size = (length_ratio * size, height_ratio * size)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Castlevania")
_normal_background = pygame.transform.scale(pygame.image.load('Assets/Background-easy.png'), (1200, 490))
window.blit(_normal_background, (0, 0))
_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height
class BackgroundEngine(ABC):
    
    @staticmethod
    def get_current_image(player_hitbox:pygame.Rect) -> pygame.Surface:
        #Return a surface with the current background image TODO
        #Preform paralax scrolling overlay here TODO
        background = pygame.Surface(window_size)
        
        return background
    
    @staticmethod
    def get_window():
        return window


    @staticmethod
    def get_current_image_frame(player_hitbox:pygame.Rect)-> pygame.Rect:
        #Return a Rect with the current global frame that the screen is on TODO
        return pygame.Rect(0, 0, window_size[0], window_size[1])
        pass
    
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
