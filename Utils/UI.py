import pygame
from Utils.number_conversion import NumberConversion


class UI:

    def __init__(self) -> None:
        score_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/Score.png'), (135, 35))]
        score_hitbox = pygame.Rect(5, 5, 135, 35)

        stage_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/stage.png'), (140, 35))]
        stage_hitbox = pygame.Rect(570, 5, 100, 35)

        time_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/time.png'), (140, 35))]
        time_hitbox = pygame.Rect(300, 5, 100, 35)

        player_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/Player.png'), (165, 35))]
        player_hitbox = pygame.Rect(5, 50, 155, 35)

        enemy_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/enemy.png'), (145, 35))]
        enemy_hitbox = pygame.Rect(5, 100, 145, 35)

        heart_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/heart.png'), (40, 30))]
        heart_hitbox = pygame.Rect(650, 50, 5, 10)

        p_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI_text/p.png'), (40, 30))]
        p_hitbox = pygame.Rect(650, 100, 5, 10)

        box_img = [pygame.transform.scale(pygame.image.load('Assets/Sprites/UI-other/inventory_box.png'), (100, 80))]
        box_hitbox = pygame.Rect(500, 50, 100, 100)

        self.all_ui = [ [score_img, score_hitbox],
                        [stage_img, stage_hitbox],
                        [time_img, time_hitbox],
                        [player_img, player_hitbox],
                        [enemy_img, enemy_hitbox], 
                        [heart_img, heart_hitbox],
                        [p_img, p_hitbox],
                        [box_img, box_hitbox]]

        self.score = "000000"
        self.time = "0000"
        self.stage = "00"
        self.heart = "00"
        self.p = "00"
        self.player_health = 16
        self.enemy_health = 16

    def change_score(self, change):
        pass

    def change_time(self, change):
        self.time = str(change)
        self.time = "0" * (4 - len(self.time)) + self.time

    def change_stage(self, change):
        pass

    def change_p(self, change):
        pass

    def change_heart(self, change):
        pass

    def get_numbers(self):
        num = NumberConversion()
        return [num.convert_score(self.score),
                num.convert_time(self.time),
                num.convert_stage(self.stage),
                num.convert_heart(self.heart),
                num.convert_p(self.p),
                num.convert_player_health(self.player_health),
                num.convert_enemy_health(self.enemy_health)]

