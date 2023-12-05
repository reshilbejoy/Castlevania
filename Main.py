from typing import List
from BackgroundEngine import BackgroundEngine
from Abstract.Player import Player
from Sprite import Sprite
class Game():
    def __init__(self):
        #initialize all sprites in this array
        self._all_sprites:List[Sprite] = []
        self._player:Player = None
        self._active_sprites:List[Sprite] = []

    def game_loop(self):
        #Main game loop logic (this should be ready to go)
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