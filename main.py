import pygame
from Player import Player
from Grid import Grid
from Enemy import Enemy
import random

pygame.init()
size = 45
height_ratio = 14
window_ratio = 22
score_box = window_ratio * 6
window_length = window_ratio * size
window_height = height_ratio * size
screen = pygame.display.set_mode((window_length, window_height + score_box))
background = pygame.Surface((window_length, window_height))
#sprite_surface = pygame.Surface((screen, (20, 210, 99)))
character_size = 100
black = (0, 0, 0)
image = pygame.image.load('Castlevania_Test_Background.jpg')
enemy = Enemy(40, window_length, window_height)
background_height = image.get_height()
background_width = image.get_width()
print(background_width)
movement_speed = 5
player = Player(100, 300, character_size, window_length, background_width, movement_speed)
grid = Grid()
print(grid.grid_return())

def offset(player, enemy):
    return int(enemy.enemy_x - player.character_pos_x), int(enemy.enemy_y - player.character_pos_y)

def game():
    
    game_over = False
    clock = pygame.time.Clock()
    print(background_height, background_width)
    FPS = 60
    while not game_over:
        pressed = pygame.key.get_pressed()
        viewpoint_x = player.move(pressed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not player.isJumping:
                    player.isJumping = True
        
        if player.isJumping:
            player.jump()
        
        enemy.move(window_length)
    
        screen.blit(image, (viewpoint_x, score_box))
        enemy.draw(screen)
        
        player.draw(screen)

        if player.mask.overlap(enemy.mask, offset(player, enemy)):
            
            player.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        pygame.display.update()
        clock.tick(FPS)

game()
    