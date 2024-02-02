from typing import Callable, List
from pygame import Rect
import pygame
from Abstract.Interaction import Interactable
from Utils.signals import DamageMessage, InventoryMessage, Item, TargetType
from background_engine import BackgroundEngine


attack_span_ms = 1000

class HarmingHitbox(Interactable):
    def __init__(self,hitbox:Rect,pose_supplier:Callable,damage_target:TargetType, remove_obj:Callable):
        super().__init__(images=[], hitbox = hitbox, damage = 7,remove_obj=remove_obj)
        self.damage_target = damage_target
        self.pose_supplier:Callable = pose_supplier
        self.images = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/Whip_attack/3.png'), True, False), (hitbox.width, hitbox.height))
        self.creation_time:int = BackgroundEngine.get_current_time()
        self.image = pygame.Surface(hitbox.size, pygame.SRCALPHA, 32)
        self.image.convert_alpha()


    def return_current_image(self) -> pygame.Surface:
        return self.image
    
    def get_damage_message(self):
        return DamageMessage(self.damage,self.damage_target)
    
    def get_inventory_message(self):
        return InventoryMessage(Item.NONE,TargetType.NONE)        
    
    @staticmethod
    def get_attack_span():
        return attack_span_ms

    def life_span(self):
        if not self.pose_supplier()[2]:
            self.damage = 0
            return False
        return True

    def _movement(self):
        self.hitbox = self.pose_supplier()[0]
