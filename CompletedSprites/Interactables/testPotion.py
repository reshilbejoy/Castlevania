from typing import List
from pygame import Rect
import pygame
from Abstract.Interaction import Interactable
from Utils.signals import DamageMessage, InventoryMessage, Item, TargetType


class testPotion(Interactable):
    def __init__(self,images, hitbox):
        super().__init__(images=[], hitbox = hitbox, damage = 1)
        self.images = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Interactables/download.jpeg'), True, False), (hitbox.width, hitbox.height))
    
    def return_current_image(self) -> pygame.Surface:
        return self.images
    
    def get_damage_message(self):
        return DamageMessage(self.damage,TargetType.PLAYER)
    
    def get_inventory_message(self):
        return InventoryMessage(Item.NONE,TargetType.PLAYER)

    def update(self):
        pass

    def life_span(self):
        return True

    def _movement(self):
        return super()._movement()