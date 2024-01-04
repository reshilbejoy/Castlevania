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
window_size = (600,500)
window = pygame.display.set_mode((length_ratio * size, height_ratio * size))
pygame.display.set_caption("Castlevania")
_normal_background = pygame.transform.scale(pygame.image.load('Assets/Background-easy.png'), (1200, 1600))
_background_arr:List[pygame.Surface] = []
_timer = pygame.time.Clock() 
_draw_frame_size:Tuple[float,float] = (500,600)  #Width, Height
_update_frame_size:Tuple[float,float] = (700,800)  #Width, Height

class BackgroundEngine(ABC):

    box_viewpoint = 0
    
    @staticmethod
    def get_current_image(player_hitbox:pygame.Rect) -> pygame.Surface:
        #Return a surface with the current background image TODO
        #Preform paralax scrolling overlay here TODO
        background = pygame.Surface(window_size)
        box_viewpoint = BackgroundEngine.get_current_image(player_hitbox)
        background.blit(_normal_background, (box_viewpoint, 22*6))
        return background


    @staticmethod
    def get_current_image_frame(player_hitbox:pygame.Rect)-> pygame.Rect:
        if not (player_hitbox.x < window_size[0] / 2 or -box_viewpoint >= (_normal_background.get_width() - window_size[0])): 
            box_viewpoint -= 5
        
        if not (player_hitbox.x > (window_size[0] / 2) or box_viewpoint >= 0):
            box_viewpoint +=5
        
        return box_viewpoint


        
    
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
