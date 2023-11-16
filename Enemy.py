import pygame

class Enemy:
    def __init__(self):
        self.image = pygame.image.load('Enemy.png')
        self.width = 80
        self.height = int(self.width * 1.6)
        self.big_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.big_image)
        self.x = 100
        self.y = 100
    
    def draw(self, screen):
        screen.blit(self.big_image, (100, 100))
