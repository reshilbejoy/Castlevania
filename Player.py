import pygame
import time

class Player:
    def __init__(self, character_width, window_width, bg_width, terminal_x, window_height, ground_height, view_height, score_box):
        self.character_height = int(character_width * 1.6)
        self.character_pos_x = 100
        self.character_pos_y = 200
        self.character_width = character_width
        self.view_width = window_width
        self.background_width = bg_width
        self.box_viewpoint_x = 0
        self.speed = 0
        self.image = pygame.transform.scale(pygame.image.load("New_Gretel.png"), (self.character_width, self.character_height))
        #self.mask = pygame.mask.from_surface(self.image)
        #self.olist = self.mask.outline()
        self.jumping_y = self.character_pos_y
        self.starting_velocity_y = -15
        self.current_velocity = 0
        self.gravity = -self.starting_velocity_y * 0.05
        self.isJumping = False
        self.isBgMoving = False
        self.horizontalForce = 0.4
        self.frictionForce = 0.3
        self.net_force = (abs(self.horizontalForce) - abs(self.frictionForce))
        self.terminal_x_velocity = terminal_x
        self.movingDir = None
        self.horizontalVelocity = self.speed
        self.rect = self.updateRect()
        self.walkLeft = [pygame.transform.scale(pygame.image.load('Sprites/Player_walk/2.png'),(self.character_width, self.character_height)), pygame.transform.scale(pygame.image.load('Sprites/Player_walk/3.png'),(self.character_width, self.character_height)), pygame.transform.scale(pygame.image.load('Sprites/Player_walk/4.png'),(self.character_width, self.character_height)), pygame.transform.scale(pygame.image.load('Sprites/Player_walk/5.png'),(self.character_width, self.character_height))]
        self.walkRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Player_walk/2.png'), True, False), (self.character_width, self.character_height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Player_walk/3.png'), True, False), (self.character_width, self.character_height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Player_walk/4.png'), True, False), (self.character_width, self.character_height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Player_walk/5.png'), True, False), (self.character_width, self.character_height))]
        self.canMove = True
    
    def updateRect(self):
        return pygame.Rect(self.character_pos_x, self.character_pos_y, self.character_width, self.character_height)

    def applyForce(self, platforms):
        collision_detection = False
        self.canMove = True
        for platform in platforms:
            if platform.player_collision(self.rect):
                #print(self.rect.bottom, platform.rect.top, platform.rect.bottom)
                #time.sleep(5)
                
                if (self.rect.bottom >= platform.rect.top and self.rect.bottom <= platform.rect.bottom) and (self.current_velocity > 0): # collides from top
                    self.current_velocity = 0
                    collision_detection = True
                    self.isJumping = False
                    self.character_pos_y = platform.rect.top - self.rect.height + 1
                    self.rect = self.updateRect()
                    break
        if not collision_detection: # collision_detection is true if there is a normal force
            #print(self.current_velocity, self.rect.top + self.rect.height)
            self.current_velocity += self.gravity
            self.character_pos_y += self.current_velocity
            self.rect = self.updateRect()


    def jump(self):
        self.isJumping = True
        self.current_velocity = self.starting_velocity_y
        self.character_pos_y += self.current_velocity
        self.rect = self.updateRect()
        #print(self.rect.top, self.character_pos_y, self.rect.height, self.current_velocity)

    def speeding_up(self):
        if self.speed < self.terminal_x_velocity:
            speed_val = self.speed + self.net_force
            self.speed = round(speed_val, 2)
    
    def move(self, pressed, enemy_x, enemy_y):

        self.left = False
        self.right = False
        self.walk_count = 0
        if self.canMove: 
            if pressed[pygame.K_RIGHT] and self.character_pos_x <= self.view_width - self.character_width and not (self.isJumping and not self.movingDir):
                self.movingDir = True
                self.speeding_up()
                if self.character_pos_x < (self.view_width / 2) or -self.box_viewpoint_x >= (self.background_width - self.view_width): 
                    new_pos = self.character_pos_x + self.speed
                    self.character_pos_x = round(new_pos, 2)
                else:
                    enemy_x -= self.speed
                    self.box_viewpoint_x -= self.speed
                self.right = True
                self.left = False
                
            elif pressed[pygame.K_LEFT] and self.character_pos_x > 0 and not (self.isJumping and self.movingDir):
                self.movingDir = False
                self.speeding_up()
                if self.character_pos_x > (self.view_width / 2) or self.box_viewpoint_x >= 0:
                    new_pos = self.character_pos_x - self.speed
                    self.character_pos_x = round(new_pos, 2)
                else:
                    enemy_x += self.speed
                    self.box_viewpoint_x += self.speed
                self.right = False
                self.left = True
                
            if not pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT] and not self.speed <= 0:
                self.net_force = self.frictionForce
                new_speed = self.speed - self.net_force
                self.speed = round(new_speed, 2)
                if self.movingDir:
                    self.character_pos_x += self.speed
                else:
                    self.character_pos_x -= self.speed
            if self.speed == 0:
                self.movingDir = None
                self.left = False
                self.right = False
                self.walkCount = 0
            self.rect = self.updateRect()
        
        #self.rect = pygame.Rect(self.character_pos_x, self.character_pos_y, self.size, self.size)
        return self.box_viewpoint_x, enemy_x, enemy_y
    
    def draw(self, screen):
        #pygame.draw.rect(screen, (1, 1, 1), self.rect)
        if self.walkCount + 1 >= 17:
             self.walkCount = 0
                
        if self.left:  
            screen.blit(self.walkLeft[int(self.walkCount//4)], (self.character_pos_x, self.character_pos_y))
            self.walkCount += 0.5                          
        elif self.right:
            screen.blit(self.walkRight[int(self.walkCount//4)], (self.character_pos_x, self.character_pos_y))
            self.walkCount += 0.5
        else:
            screen.blit(self.image, (self.character_pos_x, self.character_pos_y))
            self.walkCount = 0
        #pygame.draw.rect(screen, (1, 1, 1), self.rect)
        #screen.blit(self.image, (self.character_pos_x, self.character_pos_y))
        
