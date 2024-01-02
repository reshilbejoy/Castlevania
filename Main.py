from typing import List
from background_engine import BackgroundEngine
import pygame
from Abstract.Player import Player
from Abstract.Sprite import Sprite
from Abstract.dynamic_sprite import DynamicSprite
class Game():
    
    def __init__(self):
        #initialize all sprites in this array
        self._all_sprites:List[Sprite] = []
        self._player:Player = None
        self._active_sprites:List[Sprite] = []
        self._game_over = False

    def game_loop(self):
        
        #Main game loop logic (this should be ready to go)
        pygame.init()
        if not self.exit_condition():
            self.handle_collisions()
            self.handle_keystrokes()
            for i in self._all_sprites:
                if i.should_update():
                    i.update()
                    if i.should_draw():
                        self._active_sprites.append(i)
                        i.draw()
                else:
                    self._active_sprites.remove(i)
            
            BackgroundEngine.tick_timer()

    
    def handle_collisions(self):
        #handle collisions between Interactable objects and active dynamic sprites TODO
        pass
    
    def handle_keystrokes(self):
        pressed = pygame.key.get_pressed()
        

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    self._player.apply_force(0, 0.5)
                if event.type == pygame.K_d:
                    self._player.apply_force(0.4, 0)
                if event.type == pygame.K_a:
                    self._player.apply_force(0.4, 0)
                if event.type == pygame.K_s:
                    pass
                if event.type == pygame.K_k:
                    pass
                if event.type == pygame.K_w:
                    pass
            

    def exit_condition(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
if __name__ == "__main__":
    Castlevania = Game()
    while True:
        Castlevania.game_loop()
        pygame.quit()
    