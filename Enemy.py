import pygame

class Enemy:
    def __init__(self, enemy_size, view_width, view_height, bg_moving, bg_speed):
        self.image = pygame.image.load('Enemy.png')
        self.width = 80
        self.height = int(self.width * 1.6)
        self.enemy_x = view_width - enemy_size
        self.enemy_y = int(view_height / 2)
        self.enemy_size = enemy_size
        self.mask = pygame.mask.Mask((self.enemy_size, self.enemy_size), True)
        self.color = (20, 210, 99)
        self.speed = 5
        self.bg_speed = bg_speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.enemy_x, self.enemy_y, self.enemy_size, self.enemy_size))

    def move(self, view_width):
        self.enemy_x -= self.speed
        if (self.enemy_x <= 0 or self.enemy_x >= view_width - self.enemy_size):
            self.speed *= -1
