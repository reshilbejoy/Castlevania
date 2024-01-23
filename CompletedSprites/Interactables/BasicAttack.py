from typing import Callable, List
from pygame import Rect
import pygame
from Abstract.Interaction import Interactable
from Utils.signals import DamageMessage, InventoryMessage, Item, TargetType
from background_engine import BackgroundEngine


attack_span_ms = 250

class BasicAttack(Interactable):
    def __init__(self,hitbox,pose_supplier:Callable,damage_target:TargetType, remove_obj:Callable):
        super().__init__(images=[], hitbox = hitbox, damage = 1,remove_obj=remove_obj)
        self.damage_target = damage_target
        self.pose_supplier:Callable = pose_supplier
        self.images_right = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/Whip_attack/1.png'), False, False), (160, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/Whip_attack/2.png'), True, False), (200, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/Whip_attack/3.png'), True, False), (160, hitbox.height))] 
        self.images_left = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/Whip_attack/1.png'), False, False), (160, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/Whip_attack/2.png'), False, False), (200, hitbox.height)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/Whip_attack/3.png'), False, False), (160, hitbox.height))] 
        self.images_hit = [pygame.transform.scale(pygame.image.load('Assets/Interactables/Whip_attack/Whip_hit/1.png'), (40, 40))]
        self.creation_time:int = BackgroundEngine.get_current_time()


    def return_current_image(self) -> pygame.Surface:
        dynSpritePose:[Rect,int] = self.pose_supplier()
        if(BackgroundEngine.get_current_time() - self.creation_time < 0.3*BasicAttack.get_attack_span()):
            if dynSpritePose[1] >= 0:
                return self.images_right[0]
            else:
                return self.images_left[0]
        
        elif(BackgroundEngine.get_current_time() - self.creation_time < 0.6*(BasicAttack.get_attack_span())):

            if dynSpritePose[1] >= 0:
                return self.images_right[1]
            else:
                return self.images_left[1]
                    
        elif(BackgroundEngine.get_current_time() - self.creation_time <= 1.5*(BasicAttack.get_attack_span())):

            if dynSpritePose[1] >= 0:
                return self.images_right[2]
            else:
                return self.images_left[2]

    
    def get_damage_message(self):
        self.hit = True
        return DamageMessage(self.damage,self.damage_target)
    
    def get_inventory_message(self):
        return InventoryMessage(Item.NONE,TargetType.NONE)        
    
    @staticmethod
    def get_attack_span():
        return attack_span_ms

    def life_span(self):
        return BackgroundEngine.get_current_time() - self.creation_time<attack_span_ms

    def _movement(self):
        new_hitbox:Rect = self.get_hitbox()
        dynSpritePose:[Rect,int] = self.pose_supplier()
        # Player facing right
        if dynSpritePose[1] >= 0:
            new_hitbox.midleft = dynSpritePose[0].midright
            if(BackgroundEngine.get_current_time() - self.creation_time < 0.3*BasicAttack.get_attack_span()):
                new_hitbox.top += 3
                new_hitbox.left -= 143
            elif(BackgroundEngine.get_current_time() - self.creation_time < 0.6*(BasicAttack.get_attack_span())):
                new_hitbox.left -= 67
                new_hitbox.top -= 4
            else:
                new_hitbox.left += 20
                new_hitbox.top += 2
        # Player facing left
        else:
            new_hitbox.midright = dynSpritePose[0].midleft
            if(BackgroundEngine.get_current_time() - self.creation_time < 0.3*BasicAttack.get_attack_span()):
                new_hitbox.top += 3
                new_hitbox.left += 143
            elif(BackgroundEngine.get_current_time() - self.creation_time < 0.6*(BasicAttack.get_attack_span())):
                new_hitbox.left += 87
                new_hitbox.top -= 4
            else:
                new_hitbox.left += 40
                new_hitbox.top += 2
        
        self._hitbox = new_hitbox
