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
        self.mask = pygame.mask.Mask((self.width, self.length), True)

    def move(self, box_viewpoint):
        self.x = box_viewpoint + 300
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.length))
    
    def offset_platform(self, player):
        return int(self.x - player.character_pos_x), int(self.y - player.character_pos_y)
    
    def player_collision(self, player_x, player_y, player_height):
       """overlap = player.mask.overlap(platform.mask, offset_platform(player, platform))
        if overlap != None:
            if overlap[1] > 70:
                player.isJumping = False
            else:
                player.current_velocity *= -1"""
        