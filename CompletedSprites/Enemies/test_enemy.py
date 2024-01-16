from Abstract import Enemy
from typing import List
from abc import ABC, abstractmethod 
import pygame
from Abstract import player

from Utils.signals import DamageMessage

class Test(Enemy, ABC): 
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int):
        super.init(terminal_vel_x, terminal_vel_y, images, hitbox, health)
        