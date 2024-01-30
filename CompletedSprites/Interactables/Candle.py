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

class Candle(Interactable):
    def __init__(self, images: List[Surface], hitbox: Rect, remove_obj, create_obj):
        super().__init__(images, hitbox, 0, remove_obj)
        self.index = 0
        self._health = 1
        self.damage, self.damage_target = None, None
        self.invince_time_ms = 600
        self.last_invince_timestep = 0
        self._hit = False
        self.images_hit = [pygame.transform.scale(pygame.image.load('Assets/Interactables/Whip_attack/Whip_hit/1.png'), (20, 30))]
        self._death = [pygame.transform.scale(pygame.image.load('Assets/Enemies/Death/1.png'), (20, 30)), 
                       pygame.transform.scale(pygame.image.load('Assets/Enemies/Death/2.png'), (20, 30)), 
                       pygame.transform.scale(pygame.image.load('Assets/Enemies/Death/3.png'), (20, 30))]
        self._dead = False
        self.timestamp = 0
        self.create_obj = create_obj

    
    def update(self):
        #Platform has no update since it does not move
        pass

    def return_current_image(self) -> pygame.Surface:
        if self._health > 0:
            self.index += 0.05
            #returns first image bec platforms do not have animations
            return self._image_arr[int(self.index) % 2]
        if BackgroundEngine.get_current_time() - self.timestamp <= 300:
            return self._death[0]
        elif BackgroundEngine.get_current_time() - self.timestamp <= 900:
            return self._death[1]
        else:
            if BackgroundEngine.get_current_time() - self.timestamp > 1200:
                self._dead = True
            return self._death[2]

    def get_hitbox(self):
        return self._hitbox

    def handle_damage_interaction(self,interaction_msg: DamageMessage) -> None:
        if interaction_msg.target == (TargetType.ENEMY or TargetType.ALL_SPRITES):
            if interaction_msg.damage > 0:
                if((BackgroundEngine.get_current_time()-self.last_invince_timestep) > self.invince_time_ms):
                    self.invincible = True
                    self.last_invince_timestep = BackgroundEngine.get_current_time()
                    self._health -= interaction_msg.damage
                    self._hit = True
            else:
                 self._health -=interaction_msg.damage
            self._hit = True
            self._hit_time = BackgroundEngine.get_current_time()
        if self._health <= 0 and self.timestamp == 0:
            self.timestamp = BackgroundEngine.get_current_time()
    
    def handle_inventory_interaction(self,interaction_msg: InventoryMessage) -> None:
        pass

    @staticmethod
    def get_attack_span():
        pass

    def life_span(self):
        if not self._dead:
            return True
        else:
            return False

    def update(self):
        if self.life_span():
            self._movement()
        else:
            self.create_obj()
            self.remove_obj(self)

    def _movement(self):
        pass

    def get_damage_message(self):
        return DamageMessage(self.damage, self.damage_target)

    def get_inventory_message(self):
        return InventoryMessage(Item.NONE, TargetType.NONE)

    def check_hit(self):
        if self._hit:
            if BackgroundEngine.get_current_time()-self._hit_time >= 500:
                self._hit = False
        return self._hit

    def hit_animation(self, rect, surface):
        hitbox = self.get_hitbox()
        surface.blit(self.images_hit[0], (hitbox.left - rect.left - 17, hitbox.top - rect.top - 7))
        return surface
    
        