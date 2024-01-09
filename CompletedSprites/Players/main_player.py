from Abstract.dynamic_sprite import DynamicSprite
from typing import List
from abc import ABC, abstractmethod 
import pygame
from Abstract.Player import Player

class MainPlayer(Player):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox: pygame.Rect, health:int):
        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health)
        self.walkLeft = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/2.png'),(hitbox.width, hitbox.height)), pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/3.png'),(hitbox.width, hitbox.height)), pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/4.png'),(hitbox.width, hitbox.height)), pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/5.png'),(hitbox.width, hitbox.height))]
        self.walkRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/2.png'), True, False), (hitbox.width, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/3.png'), True, False), (hitbox.width, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/4.png'), True, False), (hitbox.width, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/5.png'), True, False), (hitbox.width, hitbox.height))] 
        self.image = pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/1.png'), (hitbox.width, hitbox.height))
        self.horizontalForce = 0.2
        self.frictionForce = 0.2
        self.net_force = (abs(self.horizontalForce) - abs(self.frictionForce))
        self.starting_velocity_y = -15
        self.verticalForce = 0
        self.current_velocity = 0
        self.speed = 0
        self.walkCount = 0
        self.left = False
        self.right = False
        
    
    def attack(self):
        return super().attack()
    
    def return_current_image(self) -> pygame.Surface:
        if self.walkCount + 1 >= 17:
             self.walkCount = 0    
        if self.left:  
            self.walkCount += 0.5
            return self.walkLeft[int(self.walkCount//4)]                
        elif self.right:
            self.walkCount += 0.5
            return self.walkRight[int(self.walkCount//4)]
        else:
            self.walkCount = 0
        return self.image