from typing import Dict, List, TypedDict
from CompletedSprites.Interactables.testPotion import testPotion
from background_engine import BackgroundEngine
import pygame
from Utils.UI import UI
from Utils.timer import Timer
from Utils.level_parser import Parser
from Abstract.Player import Player
from Abstract.Interaction import Interactable
from Abstract.Sprite import Sprite
from Abstract.dynamic_sprite import DynamicSprite
from CompletedSprites.Players.main_player import MainPlayer
from CompletedSprites.Platforms.Platform import Platform, PlatformType
from Constants.window_constants import size, length_ratio, height_ratio, height, length, background_length
from CompletedSprites.UI.static import Static_UI


DynamicSpriteTypes = {MainPlayer}
InteractableSpriteTypes = {testPotion}
PlatformSpriteTypes = {Platform}

class SortedSprites(TypedDict):
    Dynamic : List[DynamicSprite]
    Interactable : List[Interactable]
    Platform : List[Sprite]

class Game():
    
    def __init__(self):
        #initialize all sprites in this array
        
        
        self._sprite_dict: Dict[str,SortedSprites] = {"Active":{"Dynamic":[],"Interactable":[],"Platform":[]},
                             "Inactive":{"Dynamic":[],"Interactable":[],"Platform":[]}}
        self._game_over = False

        p = Parser()
        p.load_tilemap()
        p.build_level()

        self.ui = UI()
                
        self._player:MainPlayer = MainPlayer(8, 12, [], pygame.Rect(100, 100, 50, 80), 16, self.create_interatable)
        platforms = [Platform(entry[0], entry[1], entry[2]) for entry in p.built]
        all_interactables: List[Interactable] = [testPotion([],pygame.Rect(50, 200, 50, 80))]
        self.static_ui = [Static_UI(sprite[0], sprite[1]) for sprite in self.ui.all_ui]
        self._all_sprites: List[Sprite] = [self._player] + platforms + all_interactables

        self._is_paused = False

        self.timer = Timer()
    


    def game_loop(self):
        #Main game loop logic (this should be ready to go)
        pressed = pygame.key.get_pressed()

        if not self.exit_condition():
            self.handle_pauses()
            if self._is_paused is False:
                window = BackgroundEngine.get_window()
                rect, surface = BackgroundEngine.get_current_image(self._player.get_hitbox())
                pressed = pygame.key.get_pressed()
                print(self._player.get_hitbox().left)

                for i in self._all_sprites:
                    
                    if i.should_update(self._player.get_hitbox()):
                        i.update()
                        if i.should_draw(self._player.return_hitbox()):
                            if type(i) in DynamicSpriteTypes:
                                self._sprite_dict["Active"]["Dynamic"].append(i)
                            elif type(i) in InteractableSpriteTypes:
                                self._sprite_dict["Active"]["Interactable"].append(i)
                            elif type(i) in PlatformSpriteTypes:
                                self._sprite_dict["Active"]["Platform"].append(i)

                            surface = i.draw(rect, surface)
                    else:
                        if type(i) in DynamicSpriteTypes:
                            self._sprite_dict["Inactive"]["Dynamic"].append(i)
                        elif type(i) in InteractableSpriteTypes:
                            self._sprite_dict["Inactive"]["Interactable"].append(i)
                        elif type(i) in PlatformSpriteTypes:
                            self._sprite_dict["Inactive"]["Platform"].append(i)

                window.fill((0,0,0))
                self.ui.change_time(self.timer.get_time(BackgroundEngine.get_current_time()//1000))

                for i in self.static_ui:
                    window.blit(i.return_current_image(), i.get_hitbox())
                num = self.ui.get_numbers()
                for i in num:
                    for j in i:
                        window.blit(j[0], j[1])

                self.handle_keystrokes(pressed)
                self._player.apply_force(self._sprite_dict["Active"]["Platform"])
                self.handle_collisions()

                window.blit(surface, (0, 150))
                self._sprite_dict = {"Active":{"Dynamic":[],"Interactable":[],"Platform":[]},
                        "Inactive":{"Dynamic":[],"Interactable":[],"Platform":[]}}
                BackgroundEngine.tick_timer()

            #would be nice to add a pause icon sprite to the screen and destroy it upon unpause but unneeded
            else:
                pass

    def create_interatable(self, Interactable:Interactable):
        self._all_sprites.append(Interactable)
        
    def remove_interactable(self, Interactable:Interactable):
        self._all_sprites.remove(Interactable)

    def handle_collisions(self):
        for dynSprite in self._sprite_dict["Active"]["Dynamic"]:
            for interactable in self._sprite_dict['Active']["Interactable"]:
                if interactable.return_hitbox().colliderect(dynSprite.return_hitbox()):
                    dynSprite.handle_damage_interaction(interactable.get_damage_message())
                    dynSprite.handle_inventory_interaction(interactable.get_inventory_message())

        #handle collisions between Interactable objects and active dynamic sprites TODO
        pass
    
    def handle_keystrokes(self, pressed):
        left = self._player.get_hitbox().left
        if pressed[pygame.K_s] and not self._player.isJumping:
            self._player.isCrouched = True
        if pressed[pygame.K_SPACE] and not self._player.isJumping and not self._player.isFalling:
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
                if event.type == pygame.K_EdSCAPE:
                    self._is_paused = not self.is_paused


    def exit_condition(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game_over = True
                return True
        return False
    
if __name__ == "__main__":
    Castlevania = Game()
    Castlevania.timer.start()
    while not Castlevania._game_over:
        Castlevania.game_loop()
    pygame.quit()