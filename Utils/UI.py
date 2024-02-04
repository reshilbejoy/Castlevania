import pygame
from Utils.number_conversion import NumberConversion
from pygame import Surface,Rect
from enum import Enum
from Utils.signals import Item


class UI:

    def __init__(self) -> None:
        score_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/Score.png'), (150, 35))]
        score_hitbox = pygame.Rect(5, 5, 150, 35)

        stage_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/stage.png'), (140, 35))]
        stage_hitbox = pygame.Rect(570, 5, 100, 35)

        time_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/time.png'), (140, 35))]
        time_hitbox = pygame.Rect(310, 5, 100, 35)

        player_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/Player.png'), (165, 35))]
        player_hitbox = pygame.Rect(5, 50, 155, 35)

        enemy_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/enemy.png'), (145, 35))]
        enemy_hitbox = pygame.Rect(13, 100, 145, 35)
 
        heart_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/heart.png'), (90, 60))]
        heart_hitbox = pygame.Rect(570, 62, 90, 60)

        p_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/p.png'), (40, 30))]
        p_hitbox = pygame.Rect(650, 100, 5, 10)

        box_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI-other/inventory_box.png'), (100, 80))]
        box_hitbox = pygame.Rect(450, 50, 100, 100)

        self.all_ui = [ [score_img, score_hitbox],
                        [stage_img, stage_hitbox],
                        [time_img, time_hitbox],
                        [player_img, player_hitbox],
                        [enemy_img, enemy_hitbox], 
                        [heart_img, heart_hitbox],
                        #[p_img, p_hitbox],
                        [box_img, box_hitbox]]
        self.item_list = {Item.WHIP:"Assets/Interactables/Whip_attack/1.png",Item.DAGGER:"Assets/Interactables/Throwable/Cookie/1.png"}
        self.score = "000000"
        self.score_num = 0
        self.time = "0000"
        self.stage = "00"
        self.heart = "00"
        self.p = "00"
        self.weapon = Item.WHIP
        self.player_health = 16
        self.enemy_health = 16

    def change_score(self, change):
        self.score_num = self.score_num + change
        self.score = "0" * (6 - len(str(self.score_num))) + str(self.score_num)

    def change_time(self, change):
        self.time = str(change)
        self.time = "0" * (4 - len(self.time)) + self.time

    def change_stage(self, change):
        self.stage = "0" + str(change)


    def change_weapon(self, change):
        self.weapon = change
        print(self.weapon)
        if self.weapon is Item.DAGGER:
            print("Im here")
            self.all_ui[6][0] = [pygame.transform.scale(pygame.image.load(self.item_list[self.weapon]), (60, 60))]
            self.all_ui[6][1] = pygame.Rect(470, 60, 90, 90)
        else:
            self.all_ui[6][0] = [pygame.transform.scale(pygame.image.load(self.item_list[self.weapon]), (80, 110))]
            self.all_ui[6][1] = pygame.Rect(460, 60, 90, 90)


    def change_p(self, change):
        pass

    def change_heart(self, change):
        self.heart = str(change)
        if change < 10:
            self.heart = "0" + self.heart
            

    def get_numbers(self):
        num = NumberConversion()
        return [num.convert_score(self.score),
                num.convert_time(self.time),
                num.convert_stage(self.stage),
                num.convert_heart(self.heart),
                num.convert_player_health(self.player_health),
                num.convert_enemy_health(self.enemy_health)]

