from Abstract.dynamic_sprite import DynamicSprite
from typing import List
from abc import ABC, abstractmethod 
import pygame

class Player(DynamicSprite):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int):
        self.walkLeft = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/2.png'),(self.character_width, self.character_height)), pygame.transform.scale(pygame.image.load('Sprites/Player_walk/3.png'),(self.character_width, self.character_height)), pygame.transform.scale(pygame.image.load('Sprites/Player_walk/4.png'),(self.character_width, self.character_height)), pygame.transform.scale(pygame.image.load('Sprites/Player_walk/5.png'),(self.character_width, self.character_height))]
        self.walkRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/2.png'), True, False), (self.character_width, self.character_height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Player_walk/3.png'), True, False), (self.character_width, self.character_height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Player_walk/4.png'), True, False), (self.character_width, self.character_height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Player_walk/5.png'), True, False), (self.character_width, self.character_height))] 
        
        super.__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health)
    
    @abstractmethod
    def attack(self):
        pass
    
    def update(self):
        if not self.lifespan():
            del self
            
    def lifespan(self):
        return self._health>0

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
            
        
       # return super().return_current_image()d
    
