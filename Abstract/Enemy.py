from abc import abstractmethod,ABC
from typing import Callable, List
import pygame
from Abstract.dynamic_sprite import DynamicSprite
from Abstract.Interaction import Interactable
from background_engine import BackgroundEngine

class Enemy(DynamicSprite):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int, horizontal_force, create_interactable:[Callable[[Interactable],None]], remove_obj: Callable):
        self.remove_obj = remove_obj
        self._hit = False
        self.images_hit = [pygame.transform.scale(pygame.image.load('Assets/Interactables/Whip_attack/Whip_hit/1.png'), (20, 30))]
        self._death = [pygame.transform.scale(pygame.image.load('Assets/Enemies/Death/1.png'), (20, 30)), 
                       pygame.transform.scale(pygame.image.load('Assets/Enemies/Death/2.png'), (20, 30)), 
                       pygame.transform.scale(pygame.image.load('Assets/Enemies/Death/3.png'), (20, 30))]
        self._dead = False
        self.timestamp = 0
        self.got_score = False
        self.current_time = BackgroundEngine.get_current_time()

        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health,horizontal_force,create_interactable,remove_obj)

    @abstractmethod
    def attack(self):
        pass

    def update(self):
        if self.lifespan():
            self.AI()
        else:
             self.remove_obj(self)


    def lifespan(self):
        if not self._dead:
            return True
        else:
            return False
            
    @abstractmethod
    def AI(self):
        pass
    
    @abstractmethod
    def init_obj() -> None:
        pass

    def check_hit(self):
        if self._hit:
            if BackgroundEngine.get_current_time()-self._hit_time >= 500:
                self._hit = False
        return self._hit

    def hit_animation(self, rect, surface):
        hitbox = self.get_hitbox()
        surface.blit(self.images_hit[0], (hitbox.left - rect.left - 17, hitbox.top - rect.top - 7))
        return surface

    def get_score(self):
        self.got_score = True
        return self._score