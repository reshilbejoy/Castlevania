import pygame
from Player import Player
from Grid import Grid

pygame.init()
size = 45
window_length = 16 * size
window_height = 12 * size
screen = pygame.display.set_mode((window_length, window_height))
background = pygame.Surface((window_length, window_height))

character_size = 15
black = (0, 0, 0)
image = pygame.image.load('Castlevania_Test_Background.jpg')
background_height = image.get_height()
background_width = image.get_width()
print(background_width)
movement_speed = 5
player = Player(100, 300, character_size, window_length, background_width, movement_speed)
grid = Grid()
print(grid.grid_return())



def game():
    character_pos_x = 100
    character_pos_y = 100
    
    image_x = 0
    image_y = 0
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
            
    
        screen.blit(image, (viewpoint_x, 0))
        
        pygame.draw.rect(screen, (20, 210, 99), (player.character_pos_x, player.character_pos_y, character_size, character_size))
        pygame.display.update()
        clock.tick(FPS)

game()
    