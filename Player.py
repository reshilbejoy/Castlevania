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
        self.rect = pygame.Rect(self.character_pos_x, self.character_pos_y, self.size, self.size)
        self.mask = pygame.mask.Mask((self.size, self.size), True)
        self.color = (20, 210, 99)
        self.starting_velocity = -15
        self.current_velocity = self.starting_velocity
        self.acceleration = 0.5
        self.isJumping = False

    def jump(self):
        
        self.current_velocity += self.acceleration
        self.character_pos_y += self.current_velocity
        if self.current_velocity == abs(self.starting_velocity):
            self.isJumping = False
            self.current_velocity = self.starting_velocity
    
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
        self.rect = pygame.Rect(self.character_pos_x, self.character_pos_y, self.size, self.size)
        return self.box_viewpoint_x
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
