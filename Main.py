from typing import List
from BackgroundEngine import BackgroundEngine
from Player import Player
from Sprite import Sprite
class Game():
    def __init__(self):
        #initialize all sprites in this array
        self._all_sprites:List[Sprite] = []
        self._player:Player = None
        self._background_engine:BackgroundEngine = BackgroundEngine()
        self._active_sprites:List[Sprite] = []

    def game_loop(self):
        if not self.exit_condition():
            for i in self._all_sprites:
                if i.should_draw:
                    self._active_sprites.append(i)
                    i.update()
                    i.draw()
                else:
                    self._active_sprites.remove(i)
            self._background_engine.tick_timer()
    
    def handle_collisions(self):
        #handle collisions between Interactable objects and active sprites TODO
        pass
    
    def handle_keystrokes(self):
        #handle forces applied to player based on keystrokes TODO
        pass

    def exit_condition(self):
        #wether or not to quit the game
        return False
    
if __name__ == "main":
    Castlevania = Game()
    while True:
        Castlevania.game_loop()