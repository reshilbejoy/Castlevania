from typing import Callable, List
from pygame import Rect
import pygame
from Abstract.Interaction import Interactable
from Utils.signals import DamageMessage, InventoryMessage, Item, TargetType
from background_engine import BackgroundEngine


attack_span_ms = 1000

class BasicAttack(Interactable):
    def __init__(self,hitbox,pose_supplier:Callable,damage_target:TargetType, remove_obj:Callable):
        super().__init__(images=[], hitbox = hitbox, damage = 1,remove_obj=remove_obj)
        self.damage_target = damage_target
        self.pose_supplier:Callable = pose_supplier
        self.images = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/Whip_attack/3.png'), True, False), (hitbox.width, hitbox.height))
        self.creation_time:int = BackgroundEngine.get_current_time()

    def return_current_image(self) -> pygame.Surface:
        return self.images
    
    def get_damage_message(self):
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
        # Player facing left
        else:
            new_hitbox.midright = dynSpritePose[0].midleft
        self._hitbox = new_hitbox
