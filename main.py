import pygame
from Player import Player
from Grid import Grid
from Enemy import Enemy
import random
from Platform import Platform
import time

pygame.init()
size = 45
height_ratio = 14
window_ratio = 22
score_box = window_ratio * 6
movement_speed = 5
window_length = window_ratio * size
window_height = height_ratio * size
screen = pygame.display.set_mode((window_length, window_height + score_box))
background = pygame.Surface((window_length, window_height))
#sprite_surface = pygame.Surface((screen, (20, 210, 99)))
character_size = 50
black = (0, 0, 0)
image = pygame.image.load('Castlevania_Test_Background.jpg')
ground = pygame.image.load('Background-easy.png')
ground_height = ground.get_height()
ground_width = ground.get_width()
print(ground_height, ground_width)
background_height = image.get_height()
background_width = image.get_width()
print(background_width)


player = Player(character_size, window_length, background_width, movement_speed, window_height + score_box, int(ground_height / 5), window_height, score_box)
pygame.draw.rect(screen, (255, 0, 0), player.rect, 2)  
grid = Grid()
enemy = Enemy(40, window_length, window_height, player.isBgMoving, movement_speed, window_height + score_box - int(ground_height / 5))
#print(grid.grid_return())
platform = Platform(100, 10, window_length / 2, (window_height) - 50)
ground = Platform(background_width, int(ground_height / 5), 0, window_height + score_box - int(ground_height / 5))

#def offset(player, enemy):
    #return int(enemy.enemy_x - player.character_pos_x), int(enemy.enemy_y - player.character_pos_y)

platforms = [platform, ground]

def game():
    
    game_over = False
    clock = pygame.time.Clock()
    #print(background_height, background_width)
    FPS = 60
    while not game_over:
        pressed = pygame.key.get_pressed()
        viewpoint_x, enemy.enemy_x, enemy.enemy_y = player.move(pressed, enemy.enemy_x, enemy.enemy_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not player.isJumping:
                    player.jump()
        
        
        
        enemy.move(window_length)
        platform.move(player.box_viewpoint_x)
    
        screen.blit(image, (viewpoint_x, score_box))
        enemy.draw(screen)
        
        player.draw(screen)
        platform.draw(screen)
        ground.draw(screen)

        #if (enemy.enemy_x > 400):
            #print(enemy.enemy_x)
        
        player.applyForce(platforms)
            
        #if overlap != None and overlap[1] == platform.y:
            #print(overlap)
        print((enemy.enemy_x - viewpoint_x) % 5)
        #if player.mask.overlap(enemy.mask, offset(player, enemy)):
        if player.rect.colliderect(enemy.rect):
            enemy.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            #time.sleep(5)
        
        pygame.display.update()
        clock.tick(FPS)

game()
    