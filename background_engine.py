import pygame
from typing import List,Tuple
from abc import ABC

pygame.init()
window_size = (600,500)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Castlevania")

_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height
class BackgroundEngine(ABC):
    
    @staticmethod
    def get_current_image(player_hitbox:pygame.Rect) -> pygame.Surface:
        #Return a surface with the current background image TODO
        #Preform paralax scrolling overlay here TODO
        pass
    
    @staticmethod
    def get_current_image_frame(player_hitbox:pygame.Rect)-> pygame.Rect:
        #Return a Rect with the current global frame that the screen is on TODO
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
        _timer.tick()
