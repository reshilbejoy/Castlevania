from typing import List
from background_engine import BackgroundEngine
import pygame
from Abstract.Player import Player
from Abstract.Sprite import Sprite
from Abstract.dynamic_sprite import DynamicSprite
from CompletedSprites.Players.main_player import MainPlayer
from CompletedSprites.Platform import Platform, PlatformType
from Constants.window_constants import size, length_ratio, height_ratio, height, length
class Game():
    
    def __init__(self):
        #initialize all sprites in this array
        
        self._player:MainPlayer = MainPlayer(0, 0, [], pygame.Rect(100, 100, 100, 160), 5)
        self._testingGround = Platform([pygame.transform.scale(pygame.image.load('Assets/Sprites/Platform/Platform1.png'), (length, (40)))], pygame.Rect(0, 0, length, (40)), PlatformType.NORMAL_PLATFORM)
        self._active_sprites:List[Sprite] = []
        self._game_over = False
        self._all_sprites:List[Sprite] = [self._player, self._testingGround]
        self._is_paused = False

    def game_loop(self):
        
        #Main game loop logic (this should be ready to go)
        pygame.init()
        if not self.exit_condition():
            self.handle_pauses()
            if self._is_paused is False:
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
                window = BackgroundEngine.get_window()
                window.blit(BackgroundEngine.get_current_image(MainPlayer.get_hitbox()))
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
            
    # bad implementation to still allow toggle to be changed in a unpaused state, will probably need to make a smarter solution some other time 
    def handle_pauses(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    self._is_paused = not self.is_paused


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