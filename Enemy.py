import pygame

class Enemy:
    def __init__(self):
        self.image = pygame.image.load('sprite_can.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.x = 100
        self.y = 100
    
    def draw(self, screen):
        screen.blit(self.image, (100, 100))
