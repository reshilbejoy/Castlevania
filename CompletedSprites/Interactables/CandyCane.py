from typing import Callable
from pygame import Rect
import pygame
from Abstract.Interaction import Interactable
from Utils.signals import DamageMessage, InventoryMessage, Item, TargetType
from background_engine import BackgroundEngine

class CandyCane(Interactable):
    def __init__(self, hitbox, pose_supplier: Callable, damage_target: TargetType, remove_obj: Callable,di:int):
        self.attack_span_ms = 1500
        self.movement_speed = 12
        self.damage_target = damage_target
        self.pose_supplier: Callable = pose_supplier
        self.images = pygame.transform.scale(
            pygame.transform.flip(pygame.image.load('Assets/Interactables/Throwable/Fire/1.png'), True, False),
            (hitbox.width, hitbox.height))
        self.creation_time: int = BackgroundEngine.get_current_time()
        self.velocity = self.movement_speed  
        self.direction = di  
        self.initial_spawn = True
        self.damage = 4
        

        if (self.damage_target == TargetType.ENEMY):
            self.damage = 2
            self.attack_span_ms = 1250
            self.movement_speed = 6

        super().__init__(images=[], hitbox=hitbox, damage=self.damage, remove_obj=remove_obj)

    def return_current_image(self) -> pygame.Surface:
        return self.images

    def get_damage_message(self):
        return DamageMessage(self.damage, self.damage_target)

    def get_inventory_message(self):
        return InventoryMessage(Item.NONE, TargetType.NONE)

    
    def get_attack_span(self):
        return self.attack_span_ms

    def life_span(self):
        return BackgroundEngine.get_current_time() - self.creation_time < self.attack_span_ms

    def _movement(self):
        new_hitbox: Rect = self.get_hitbox()
        dynSpritePose: [Rect, int] = self.pose_supplier()


        if self.initial_spawn:
        
            new_hitbox.midleft = dynSpritePose[0].midright
            new_hitbox.y = dynSpritePose[0].y  
            new_hitbox.x += 5 
            self.initial_spawn = False
        else:
        
            new_hitbox.x += self.direction * self.velocity
            new_hitbox.y = new_hitbox.y
        self._hitbox = new_hitbox