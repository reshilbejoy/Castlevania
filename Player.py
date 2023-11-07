import pygame

class Player:
    def __init__(self, x, y):
        self.character_pos_x = x
        self.character_pos_y = y
    def move(self, pressed):
        if pressed[pygame.K_UP]:
            self.character_pos_y -= 10
        if pressed[pygame.K_DOWN]:
            self.character_pos_y += 10
        if pressed[pygame.K_RIGHT]:
            self.character_pos_x += 10
        if pressed[pygame.K_LEFT]:
            self.character_pos_x -= 10