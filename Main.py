from typing import List
from background_engine import BackgroundEngine
import pygame
from Abstract.Player import Player
from Abstract.Sprite import Sprite
from Abstract.dynamic_sprite import DynamicSprite
from CompletedSprites.Players.main_player import MainPlayer
class Game():
    
    def __init__(self):
        #initialize all sprites in this array
        
        self._player:MainPlayer = MainPlayer(0, 0, [], pygame.Rect(100, 100, 100, 160), 5)
        self._active_sprites:List[Sprite] = [self._player]
        self._game_over = False
        self._all_sprites:List[Sprite] = [self._player]

    def game_loop(self):
        
        #Main game loop logic (this should be ready to go)
        pygame.init()
        if not self.exit_condition():
            self.handle_collisions()
            self.handle_keystrokes()
            for i in self._all_sprites:
                if i.should_update(self._player.get_hitbox()):
                    i.update()
                    if i.should_draw(self._player.return_hitbox()):
                        self._active_sprites.append(i)
                        i.draw(BackgroundEngine.get_window())
                else:
                    ...
                    #self._active_sprites.remove(i)
            
            BackgroundEngine.tick_timer()

    
    def handle_collisions(self):
        #handle collisions between Interactable objects and active dynamic sprites TODO
        pass
    
    def handle_keystrokes(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    pass # change y velocity here
                if event.type == pygame.K_d:
                    self._player.change_force(0.4, 0)
                if event.type == pygame.K_a:
                    self._player.change_force(-0.4, 0)
                if event.type == pygame.K_s:
                    pass
                if event.type == pygame.K_k:
                    pass
                if event.type == pygame.K_w:
                    pass
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_d:
                    self._player.change_force(-0.2, 0)
                if event.type == pygame.K_a:
                    self._player.change_force(0.2, 0)
            
            

    def exit_condition(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game_over = True
                return True
        return False
    
if __name__ == "__main__":
    Castlevania = Game()
    while not Castlevania._game_over:
        Castlevania.game_loop()
    pygame.quit()