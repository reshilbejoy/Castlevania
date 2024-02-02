from typing import List
import pygame
from Abstract.Sprite import Sprite
from Abstract.Interaction import Interactable
import pygame
from pygame import Surface,Rect
from enum import Enum
from background_engine import BackgroundEngine
from Abstract.Interaction import Interactable 
from Utils.signals import DamageMessage, InventoryMessage, Item, TargetType
from typing import Callable


class Heart(Interactable):
    def __init__(self, hitbox: Rect, remove_obj):
        super().__init__([], hitbox, 0, remove_obj)
        self._health = 1
        self.image = pygame.transform.scale(pygame.image.load('Assets/Sprites/Additional_sprites/Heart/1.png'), (hitbox.width, hitbox.height))
        self.damage, self.damage_target = None, None
        self._dead = False
        self.timestamp = BackgroundEngine.get_current_time()
        self.life_ms = 1000
        self.invince_time_ms = 0
        self.last_invince_timestep = 0
        self._given_heart = False

    def update(self):
        #Platform has no update since it does not move
        pass

    def return_current_image(self) -> pygame.Surface:
        return self.image
        

    def get_hitbox(self):
        return self.hitbox

    def handle_damage_interaction(self,interaction_msg: DamageMessage):
        if interaction_msg.target == (TargetType.ENEMY or TargetType.ALL_SPRITES):
            if interaction_msg.damage > 0:
                if((BackgroundEngine.get_current_time()-self.last_invince_timestep) > self.invince_time_ms):
                    self._health -= interaction_msg.damage
                    self._dead = True
                    return True
            else:
                self._health -= interaction_msg.damage
                return False
    
    def handle_inventory_interaction(self,interaction_msg: InventoryMessage) -> None:
        pass

    @staticmethod
    def get_attack_span():
        pass

    def life_span(self):
        if not self._dead and BackgroundEngine.get_current_time() - self.timestamp < self.life_ms:
            return True
        else:
            return False

    def update(self):
        if self.life_span():
            self._movement()
        else:
            self.remove_obj(self)

    def _movement(self):
        pass

    def get_damage_message(self):
        return DamageMessage(self.damage, self.damage_target)

    def get_inventory_message(self):
        return InventoryMessage(Item.NONE, TargetType.NONE)

        