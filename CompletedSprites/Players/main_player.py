from Abstract.dynamic_sprite import DynamicSprite
from typing import List
from abc import ABC, abstractmethod 
import pygame
from Abstract.Player import Player

class MainPlayer(Player):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox: pygame.Rect, health:int):
        self.horizontalForce = 0.2
        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health, self.horizontalForce)
        self.walkLeft = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/2.png'),(hitbox.width, hitbox.height)), pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/3.png'),(hitbox.width, hitbox.height)), pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/4.png'),(hitbox.width, hitbox.height)), pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/5.png'),(hitbox.width, hitbox.height))]
        self.walkRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/2.png'), True, False), (hitbox.width, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/3.png'), True, False), (hitbox.width, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/4.png'), True, False), (hitbox.width, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/5.png'), True, False), (hitbox.width, hitbox.height))] 
        self.image = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/1.png'), True, False), (hitbox.width, hitbox.height))
        self.jump_animation_right = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_jump/1.png'), True, False), (hitbox.width, hitbox.height))
        self.jump_animation_left = pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_jump/1.png'),(hitbox.width, hitbox.height))
        self.fall_animation_right = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_fall/1.png'), True, False), (hitbox.width, hitbox.height))
        self.fall_animation_left = pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_fall/1.png'),(hitbox.width, hitbox.height))
        self.verticalForce = 0
        self.walkCount = 0
        
        
        
    
    def attack(self):
        return super().attack()
    
    def return_current_image(self) -> pygame.Surface:

        if self.isFalling and self.left:
            return self.fall_animation_left
        elif self.isFalling:
            print("f")
            return self.fall_animation_right


        if self.isJumping and self.left:
            return self.jump_animation_left
        elif self.isJumping:
            return self.jump_animation_right
        
        if self.walkCount + 1 >= 17:
             self.walkCount = 0    
        if self.left:  
            self.walkCount += 0.5
            return self.walkLeft[int(self.walkCount//4) - 1]                
        elif self.right:
            self.walkCount += 0.5
            return self.walkRight[int(self.walkCount//4) - 1]
        else:
            self.walkCount = 0
    
        return self.image