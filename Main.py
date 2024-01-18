from typing import List
from background_engine import BackgroundEngine
import pygame
from Utils.level_parser import Parser
from Abstract.Player import Player
from Abstract.Interaction import Interactable

from Abstract.Sprite import Sprite
from Abstract.dynamic_sprite import DynamicSprite
from CompletedSprites.Players.main_player import MainPlayer
from CompletedSprites.Platform import Platform, PlatformType
from Constants.window_constants import size, length_ratio, height_ratio, height, length, background_length
class Game():
    
    def __init__(self):
        #initialize all sprites in this array
        
        self._player:MainPlayer = MainPlayer(8, 7, [], pygame.Rect(100, 100, 50, 80), 5)
        self._active_sprites:List[Sprite] = []
        self._all_interactables: List[Interactable] = []
        self._game_over = False
        p = Parser()
        p.load_tilemap()
        p.build_level()
        platforms = [Platform(entry[0], entry[1], entry[2]) for entry in p.built]
        self._all_sprites: List[Sprite] = [self._player] + platforms
        #print(len(platforms))
        self._all_plat = platforms
        self._is_paused = False
    


    def game_loop(self):
        #Main game loop logic (this should be ready to go)
        #print(self._player.get_hitbox().left)
        pressed = pygame.key.get_pressed()
        if not self.exit_condition():
            self.handle_pauses()
            if self._is_paused is False:
                window = BackgroundEngine.get_window()
                rect, surface = BackgroundEngine.get_current_image(self._player.get_hitbox())
                #window.blit(surface, (0,0))
                pressed = pygame.key.get_pressed()
                self.handle_collisions()
                self.handle_keystrokes(pressed)
                #print(self._player.net_force)
                self._player.apply_force(self._all_plat)
                
                for i in self._all_sprites:
                    
                    if i.should_update(self._player.get_hitbox()):
                        i.update()
                    if i.should_draw(self._player.return_hitbox()):
                        self._active_sprites.append(i)

                        surface = i.draw(rect, surface)
                        
                    else:
                        ...
                        #self._active_sprites.remove(i)
                window.blit(surface, (0, 150))
                BackgroundEngine.tick_timer()

            #would be nice to add a pause icon sprite to the screen and destroy it upon unpause but unneeded
            else:
                pass

    @staticmethod
    def create_interatable(self, Interactable:Interactable):
        self._all_sprites.append(Interactable)
        self._all_interactables.append(Interactable)
        
    @staticmethod
    def remove_interactable(self, Interactable:Interactable):
        self._all_sprites.remove(Interactable)
        self._all_interactables.remove(Interactable)

    def handle_collisions(self):
        #handle collisions between Interactable objects and active dynamic sprites TODO
        pass
    
    def handle_keystrokes(self, pressed):
        left = self._player.get_hitbox().left
        if pressed[pygame.K_s] and not self._player.isJumping:
            self._player.isCrouched = True
        if pressed[pygame.K_SPACE] and not self._player.isJumping:
            self._player.jump()
        if pressed[pygame.K_d] and (left < background_length):
            self._player.change_force(0.4, 0)
        if pressed[pygame.K_a] and (left > 0):
            self._player.change_force(-0.4, 0)
        if not (pressed[pygame.K_d] or pressed[pygame.K_a]):
            self._player.change_force(0, 0)
        if pressed[pygame.K_k]:
            pass
        if pressed[pygame.K_w]:
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
                self._game_over = True
                return True
        return False
    
if __name__ == "__main__":
    Castlevania = Game()
    while not Castlevania._game_over:
        Castlevania.game_loop()
    pygame.quit()