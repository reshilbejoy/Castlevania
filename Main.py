from typing import Dict, List
from typing_extensions import TypedDict
from CompletedSprites.Enemies.Ghoul import Ghoul
from CompletedSprites.Interactables.BasicAttack import BasicAttack
from CompletedSprites.Interactables.HarmingHitbox import HarmingHitbox
from CompletedSprites.Interactables.testPotion import testPotion
from Abstract.Enemy import Enemy
from Utils.signals import TargetType
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
from Constants.window_constants import *
from CompletedSprites.UI.static import Static_UI
import time
from CompletedSprites.Doors.Door import Door


DynamicSpriteTypes = {MainPlayer,Ghoul}
InteractableSpriteTypes = {testPotion,BasicAttack,HarmingHitbox}
PlatformSpriteTypes = {Platform}
DoorSpriteTypes = {Door}


class SortedSprites(TypedDict):
    Dynamic : List[DynamicSprite]
    Interactable : List[Interactable]
    Platform : List[Sprite]
    Door : List[Door]

class Game():
    
    def __init__(self, level):
        #initialize all sprites in this array
        
        
        self._sprite_dict: Dict[str,SortedSprites] = {"Active":{"Dynamic":[],"Interactable":[],"Platform":[], "Door": []},
                             "Inactive":{"Dynamic":[],"Interactable":[],"Platform":[], "Door": []}}
        self._game_over = False
        self._game_started = False
        self.level = level

        p = Parser(level)
        p.load_tilemap()
        p.build_level()

        self.ui = UI()
                
        self._player:MainPlayer = MainPlayer(5, 12, [], pygame.Rect(100, 100, 50, 80), 16, self.create_object,self.remove_object)
        self._enemies:Enemy = [Ghoul(5, 12, [], pygame.Rect(200, 100, 50, 80), 5, 0.4, self.create_object,self.remove_object,self._player.get_hitbox)]
        terrain = p.built
        platforms = [Platform(entry[0], entry[1], entry[2]) for entry in terrain['Platform']]
        self.doors = [Door(entry[0], entry[1]) for entry in terrain['Door']]
        all_interactables: List[Interactable] = []
        self.static_ui = [Static_UI(sprite[0], sprite[1]) for sprite in self.ui.all_ui]
        self._all_sprites: List[Sprite] = self.doors + [self._player] + platforms + all_interactables + self._enemies

        self._is_paused = False
        self._font = pygame.font.SysFont("couriernew", 50)
        self._intro_font = pygame.font.Font('Assets/Background/controls.ttf', (9 + int(size / 8)))
        self._controls_font = pygame.font.Font('Assets/Background/controls.ttf', 18)
        self._title_font = pygame.font.Font('Assets/Background/controls.ttf', 20)
        fonts = pygame.font.get_fonts()
        self.current_map = p.get_current_map()
        self.starting_screen_position = height + score_box_height + 50

        self.timer = Timer()
    
    def fade_screen(self, window):
        fade_out = pygame.Surface((length, height + score_box_height))
        fade_out.fill((0, 0, 0))
        for alpha in (range(0, 100)):
            fade_out.set_alpha(alpha)
            window.blit(fade_out, (0, 0))
            BackgroundEngine.tick_timer()
            time.sleep(0.001)

    def controls_screen(self):
        window = BackgroundEngine.get_window()
        controls_done = False
        while not controls_done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.fade_screen(window)
                        controls_done = True
            window.fill((0, 0, 0))
            bg = pygame.transform.scale(pygame.image.load('Assets/Background/picture_controls.png'), (length, height + score_box_height))
            window.blit(bg, (0, 0))
            '''
            top_text = self._title_font.render("Controls", 1, (255, 255, 255))
            top_rect = top_text.get_rect(center=((length / 2), (height / 10)))
            bottom_text = self._title_font.render("Push 1 to Begin", 1, (255, 255, 255))
            bottom_rect = bottom_text.get_rect(center=((length / 2), (height * 1.25)))
            window.blit(top_text, top_rect)
            window.blit(bottom_text, bottom_rect)
            left_texts = [
                self._controls_font.render("D - Move Right", 1, (7, 240, 201)),
                self._controls_font.render("A - Move Left", 1, (38, 240, 122)),
                self._controls_font.render("Q - Enter Doors", 1, (240, 247, 104)),
            ]
            right_texts = [
                self._controls_font.render("SPACE - Jump", 1, (118, 164, 245)),
                self._controls_font.render("S - Crouch", 1, (190, 127, 245)),
                self._controls_font.render("K - Attack", 1, (245, 108, 199)),
            ]
            for index in range(0, len(left_texts)):
                left_text = left_texts[index]
                right_text = right_texts[index]
                left_rect = left_text.get_rect(center=((length / 3.5), ((index + 0.8) * (height / 3))))
                right_rect = right_text.get_rect(center=((length / 1.35), ((index + 1.3) * (height / 3))))
                window.blit(left_text, left_rect)
                window.blit(right_text, right_rect)'''
            BackgroundEngine.tick_timer()



            

    def starting_screen(self):
        window = BackgroundEngine.get_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self._game_started = True
                    self.fade_screen(window)
                    return
        window.blit(pygame.transform.scale(pygame.image.load('Assets/Background/CVBG.png'), (length, height + score_box_height)), (0, self.starting_screen_position))
        if self.starting_screen_position > 0:
            self.starting_screen_position -= 5
        else:
            text = self._intro_font.render("Press 1 to Start", 1, (255, 255, 255))
            rect = text.get_rect(center=(length * 0.52, self.starting_screen_position + height * 0.7))
            window.blit(text, rect)
        BackgroundEngine.tick_timer()
        
    def ending_screen(self):
        window = BackgroundEngine.get_window()
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self._game_started = True
                    self._game_over = False
                    Castlevania.__init__()
                    run_game()
        BackgroundEngine.tick_timer()
                    


    def game_loop(self):
        #Main game loop logic (this should be ready to go)
        pressed = pygame.key.get_pressed()
        window = BackgroundEngine.get_window()
        if not self.exit_condition():
            self.handle_pauses()
            if self._is_paused is False:
                
                rect, surface = BackgroundEngine.get_current_image(self._player.get_hitbox())
                pressed = pygame.key.get_pressed()

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
                            elif type(i) in DoorSpriteTypes:
                                self._sprite_dict["Active"]["Door"].append(i)

                            surface = i.draw(rect, surface)
                    else:
                        if type(i) in DynamicSpriteTypes:
                            self._sprite_dict["Inactive"]["Dynamic"].append(i)
                        elif type(i) in InteractableSpriteTypes:
                            self._sprite_dict["Inactive"]["Interactable"].append(i)
                        elif type(i) in PlatformSpriteTypes:
                            self._sprite_dict["Inactive"]["Platform"].append(i)
                        elif type(i) in DoorSpriteTypes:
                            self._sprite_dict["Inactive"]["Door"].append(i)

                window.fill((0,0,0))
                self.ui.player_health = self._player.get_health()
                self.ui.change_stage(self.level)
                self.ui.change_time(self.timer.get_time(BackgroundEngine.get_current_time()//1000))
                for i in self.static_ui:
                    window.blit(i.return_current_image(), i.get_hitbox())
                num = self.ui.get_numbers()
                for i in num:
                    for j in i:
                        window.blit(j[0], j[1])

                self.handle_keystrokes(pressed)
                for i in self._sprite_dict["Active"]["Dynamic"]:
                    i.apply_force(self._sprite_dict["Active"]["Platform"])
                self.handle_collisions()

                window.blit(surface, (0, 150))
                self._sprite_dict = {"Active":{"Dynamic":[],"Interactable":[],"Platform":[], "Door": []},
                        "Inactive":{"Dynamic":[],"Interactable":[],"Platform":[], "Door": []}}

                BackgroundEngine.tick_timer()

            #would be nice to add a pause icon sprite to the screen and destroy it upon unpause but unneeded
            else:
                pass
        else:
            self.fade_screen(window)
            self._game_started = False
            self._game_over = True

    def create_object(self, obj):
        self._all_sprites.append(obj)
        
    def remove_object(self, obj):
        self._all_sprites.remove(obj)

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
        window = BackgroundEngine.get_window()
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
            self._player.attack()
        if pressed[pygame.K_w]:
            pass
        if pressed[pygame.K_q]:
            if (self._player.inside_door(self.doors[0])):
                self.fade_screen(window)
                run_game(Game(self.level + 1))
                

            

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
                pygame.quit()
        if not self._player.lifespan():
            return True
        return False
    
    def init_sprites(self):
        for i in self._all_sprites:
            if type(i) in DynamicSpriteTypes:
                i.init_obj()


def run_game(game: Game):
    game.timer.start()
    while not game._game_over:
        game.game_loop()
    game.timer.reset(0)
    while not game._game_started:
        game.ending_screen()
    
if __name__ == "__main__":
    Castlevania = Game(1)
    while not Castlevania._game_started:
        Castlevania.starting_screen()
    Castlevania.controls_screen()
    Castlevania.init_sprites()
    run_game(Castlevania)