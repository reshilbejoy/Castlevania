import pygame
from Player import Player

class Platform:
    def __init__(self, width, length, x, y):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.speed = -5
        self.color = (178, 172, 19)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.length)

    def move(self, box_viewpoint):
        self.x = box_viewpoint + 300
        self.rect.left = self.x
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    
    def player_collision(self, player_rect):
        if self.rect.colliderect(player_rect):
            if abs(player_rect.top + player_rect.height - self.rect.top) == 1: # using 1 as offset
                return True
        return False
       
        