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

    def move(self, box_viewpoint):
        self.x = box_viewpoint + 300
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.length))
    
    def collide(self, player_x, player_y, player_height):
        ...
        