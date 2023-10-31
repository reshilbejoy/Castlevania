import pygame

pygame.init()
window_length = 1200
window_height = int(window_length / 2)
screen = pygame.display.set_mode((window_length, window_height))
black = (0, 0, 0)



def game():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ...
    
        screen.fill(black)
        pygame.draw.rect(screen, (20, 210, 99), (100, 100, 60, 60))
        pygame.display.update()

game()
    