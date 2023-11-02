import pygame

pygame.init()
window_length = 1200
window_height = int(window_length / 2)
screen = pygame.display.set_mode((window_length, window_height))
background = pygame.Surface((window_length, window_height))
black = (0, 0, 0)
image = pygame.image.load('Castlevania_Test_Background.jpg')




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
        if pressed[pygame.K_UP]:
            character_pos_y -= 10
            image_y += 5
        if pressed[pygame.K_DOWN]:
            character_pos_y += 10
            image_y -= 5
        if pressed[pygame.K_RIGHT]:
            character_pos_x += 10
            image_x -= 5
        if pressed[pygame.K_LEFT]:
            character_pos_x -= 10
            image_x += 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_over = True
            
    
        screen.blit(image, (image_x, image_y))
        pygame.draw.rect(screen, (20, 210, 99), (character_pos_x, character_pos_y, character_size, character_size))
        pygame.display.update()
        clock.tick(FPS)

game()
    