import pygame

class Player:
    def __init__(self, x, y, character_width, window_width, bg_width, speed):
        
        self.character_pos_x = x
        self.character_pos_y = y
        self.character_width = character_width
        self.character_height = int(self.character_width * 1.6)
        self.view_width = window_width
        self.background_width = bg_width
        self.box_viewpoint_x = 0
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load("New_Gretel.png"), (self.character_width, self.character_height))
        self.mask = pygame.mask.from_surface(self.image)
        self.jumping_y = self.character_pos_y
        self.starting_velocity = -8
        self.current_velocity = self.starting_velocity
        self.acceleration = 0.3
        self.isJumping = False

    def jump(self):
        
        self.current_velocity += self.acceleration
        self.character_pos_y += self.current_velocity
        if self.current_velocity >= abs(self.starting_velocity) or self.character_pos_y >= self.jumping_y:
            self.jumping_y = self.character_pos_y
            self.isJumping = False
            self.current_velocity = self.starting_velocity
    
    def move(self, pressed):
        if pressed[pygame.K_UP]:
            self.character_pos_y -= self.speed
        if pressed[pygame.K_DOWN]:
            self.character_pos_y += self.speed
        if pressed[pygame.K_RIGHT] and self.character_pos_x <= self.view_width - self.character_width:
            if self.character_pos_x < (self.view_width / 2) or -self.box_viewpoint_x >= (self.background_width - self.view_width): 
                self.character_pos_x += self.speed
            else:
                self.box_viewpoint_x -= self.speed
        if pressed[pygame.K_LEFT] and self.character_pos_x > 0:
            if self.character_pos_x > (self.view_width / 2) or self.box_viewpoint_x >= 0:
                self.character_pos_x -= self.speed
            else:
                self.box_viewpoint_x += self.speed
        #self.rect = pygame.Rect(self.character_pos_x, self.character_pos_y, self.size, self.size)
        return self.box_viewpoint_x
    
    def draw(self, screen):
        screen.blit(self.image, (self.character_pos_x, self.character_pos_y))
