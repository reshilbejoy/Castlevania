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
        self.speed = 0
        self.image = pygame.transform.scale(pygame.image.load("New_Gretel.png"), (self.character_width, self.character_height))
        self.mask = pygame.mask.from_surface(self.image)
        self.jumping_y = self.character_pos_y
        self.starting_velocity_y = -10
        self.current_velocity = self.starting_velocity_y
        self.gravity = -self.starting_velocity_y * 0.05
        self.isJumping = False
        self.isBgMoving = False
        self.horizontalForce = 0.1
        self.terminal_x_velocity = speed
        self.isMoving = False
        

    def jump(self):
        
        self.current_velocity += self.gravity
        self.character_pos_y += self.current_velocity
        if self.current_velocity >= abs(self.starting_velocity_y) or self.character_pos_y >= self.jumping_y:
            self.jumping_y = self.character_pos_y
            self.isJumping = False
            self.current_velocity = self.starting_velocity_y
    
    def move(self, pressed, enemy_x, enemy_y):
        #if pressed[pygame.K_UP]:
            #self.character_pos_y -= self.speed
        #if pressed[pygame.K_DOWN]:
            #self.character_pos_y += self.speed
        if pressed[pygame.K_RIGHT] and self.character_pos_x <= self.view_width - self.character_width:
            if self.speed < self.terminal_x_velocity:
                self.speed += self.horizontalForce
            if self.character_pos_x < (self.view_width / 2) or -self.box_viewpoint_x >= (self.background_width - self.view_width): 
                self.character_pos_x += self.speed
            else:
                enemy_x -= self.speed
                self.box_viewpoint_x -= self.speed
            
        if pressed[pygame.K_LEFT] and self.character_pos_x > 0:
            if self.character_pos_x > (self.view_width / 2) or self.box_viewpoint_x >= 0:
                self.character_pos_x -= self.speed
            else:
                enemy_x += self.speed
                self.box_viewpoint_x += self.speed
        if not pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT]:
            self.speed = 0
        #self.rect = pygame.Rect(self.character_pos_x, self.character_pos_y, self.size, self.size)
        return self.box_viewpoint_x, enemy_x, enemy_y
    
    def draw(self, screen):
        screen.blit(self.image, (self.character_pos_x, self.character_pos_y))
