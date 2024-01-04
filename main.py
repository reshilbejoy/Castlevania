from typing import List
from background_engine import BackgroundEngine
import pygame
from Abstract.player import Player
from Abstract.sprite import Sprite
class Game():
    
    def __init__(self):
        #initialize all sprites in this array
        BackgroundEngine.initBackground()
        self._all_sprites:List[Sprite] = []
        self._player:Player = None
        self._active_sprites:List[Sprite] = []
        self._is_paused = False
        BackgroundEngine.initBackground()

    def game_loop(self):
        #Main game loop logic (this should be ready to go)
        if not self.exit_condition():
            self.handle_pauses()
            if self._is_paused is False:
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
            #would be nice to add a pause icon sprite to the screen and destroy it upon unpause but unneeded
            else:
                pass

    
    def handle_collisions(self):
        #handle collisions between Interactable objects and active dynamic sprites TODO
        pass
    
    def handle_keystrokes(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    self._player.apply_force(0, 0.5)
                if event.type == pygame.K_d:
                    self._player.apply_force(0.4, 0)
                if event.type == pygame.K_a:
                    self._player.apply_force(-0.4, 0)
                if event.type == pygame.K_s:
                    pass
                if event.type == pygame.K_k:
                    pass
                if event.type == pygame.K_w:
                    pass
    
    # bad implementation to still allow toggle to be changed in a unpaused state, will probably need to make a smarter solution some other time 
    def handle_pauses(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    self._is_paused = not self.is_paused

    def exit_condition(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
if __name__ == "__main__":
    Castlevania = Game()
    while True:
        Castlevania.game_loop()
