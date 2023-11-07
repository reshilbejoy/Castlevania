import pygame
from Player import Player
from Grid import Grid

pygame.init()
size = 45
window_length = 16 * size
window_height = 12 * size
screen = pygame.display.set_mode((window_length, window_height))
background = pygame.Surface((window_length, window_height))
black = (0, 0, 0)
image = pygame.image.load('Castlevania_Test_Background.jpg')
player = Player(100, 300)
grid = Grid()
print(grid.grid_return())



def game():
    character_pos_x = 100
    character_pos_y = 100
    character_size = 60
    image_x = 0
    image_y = 0
    game_over = False
    clock = pygame.time.Clock()
    FPS = 60
    while not game_over:
        pressed = pygame.key.get_pressed()
        player.move(pressed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_over = True
            
    
        screen.blit(image, (image_x, image_y))
        pygame.draw.rect(screen, (20, 210, 99), (player.character_pos_x, player.character_pos_y, character_size, character_size))
        pygame.display.update()
        clock.tick(FPS)

game()
    