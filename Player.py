import pygame

class Player:
    def __init__(self, x, y, character_size, width, bg_width, speed):
        self.character_pos_x = x
        self.character_pos_y = y
        self.size = character_size
        self.view_width = width
        self.background_width = bg_width
        self.box_viewpoint_x = 0
        self.speed = speed

    
    def move(self, pressed):
        if pressed[pygame.K_UP]:
            self.character_pos_y -= self.speed
        if pressed[pygame.K_DOWN]:
            self.character_pos_y += self.speed
        if pressed[pygame.K_RIGHT] and self.character_pos_x <= self.view_width - self.size:
            if self.character_pos_x < (self.view_width / 2) or -self.box_viewpoint_x >= (self.background_width - self.view_width): 
                self.character_pos_x += self.speed
            else:
                self.box_viewpoint_x -= self.speed
        if pressed[pygame.K_LEFT] and self.character_pos_x > 0:
            if self.character_pos_x > (self.view_width / 2) or self.box_viewpoint_x >= 0:
                self.character_pos_x -= self.speed
            else:
                self.box_viewpoint_x += self.speed

        return self.box_viewpoint_x
