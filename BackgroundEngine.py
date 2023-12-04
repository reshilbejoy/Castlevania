import pygame
from typing import List,Tuple
from abc import ABC

_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_frame_size:Tuple[float,float] = (500,600)  #Width, Height
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
    def get_current_time()-> float:
        _timer.get_time()
        pass

    @staticmethod
    def tick_timer()-> float:
        _timer.tick()
        pass