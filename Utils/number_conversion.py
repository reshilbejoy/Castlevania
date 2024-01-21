import pygame


class NumberConversion:

    def __init__(self) -> None:

        self.dict = {
            "0": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/0.png'), (20, 35)),
            "1": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/1.png'), (20, 35)),
            "2": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/2.png'), (20, 35)),
            "3": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/3.png'), (20, 35)),
            "4": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/4.png'), (20, 35)),
            "5": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/5.png'), (20, 35)),
            "6": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/6.png'), (20, 35)),
            "7": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/7.png'), (20, 35)),
            "8": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/8.png'), (20, 35)),
            "9": pygame.transform.scale(pygame.image.load('Assets/Sprites/Numbers/9.png'), (20, 35)),
            "ph": pygame.transform.scale(pygame.image.load('Assets/Sprites/UI-other/Healthbar_p.png'), (20, 35)),
            "eh": pygame.transform.scale(pygame.image.load('Assets/Sprites/UI-other/Healthbar_e.png'), (20, 35))
        }

    def convert_score(self, score):
        list_ = []
        for number in score:
            list_.append([self.dict[number], (len(list_) * 20 + 160, 5)])
        return list_


    def convert_time(self, time):
        list_ = []
        for number in time:
            list_.append([self.dict[number], (len(list_) * 20 + 450, 5)])
        return list_

    def convert_stage(self, stage):
        list_ = []
        for number in stage:
            list_.append([self.dict[number], (len(list_) * 20 + 720, 5)])
        return list_

    def convert_p(self, p):
        list_ = []
        for number in p:
            list_.append([self.dict[number], (len(list_) * 20 + 700, 100)])
        return list_

    def convert_heart(self, heart):
        list_ = []
        for number in heart:
            list_.append([self.dict[number], (len(list_) * 20 + 700, 50)])
        return list_

    def convert_player_health(self, health):
        list_ = []
        for number in range(health):
            list_.append([self.dict["ph"], (len(list_) * 15 + 180, 50)])
        return list_

    def convert_enemy_health(self, health):
        list_ = []
        for number in range(health):
            list_.append([self.dict["eh"], (len(list_) * 15 + 160, 100)])
        return list_

