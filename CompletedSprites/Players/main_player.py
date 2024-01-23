from typing import Callable, List
import pygame
from Abstract.Player import Player
from Abstract.Interaction import Interactable
from CompletedSprites.Interactables.BasicAttack import BasicAttack
from Utils.signals import DamageMessage, InventoryMessage, Item, TargetType
from background_engine import BackgroundEngine

class MainPlayer(Player):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox: pygame.Rect,
                  health:int,create_obj:[Callable[[Interactable],None]],remove_obj:Callable):
        self.horizontalForce = 0.2
        self.starting_velocity_y = -7
        super().__init__(terminal_vel_x, terminal_vel_y, images, hitbox, health, self.horizontalForce,create_obj,remove_obj)
        self.walkLeft = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/2.png'),(hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/3.png'),(hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/4.png'),(hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_walk/5.png'),(hitbox.width, hitbox.height))]
        
        self.walkRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/2.png'), True, False), (hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/3.png'), True, False), (hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/4.png'), True, False), (hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/5.png'), True, False), (hitbox.width, hitbox.height))] 
        
        self.image = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/1.png'), True, False), (hitbox.width, hitbox.height))
        self.jump_animation_right = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_jump/1.png'), True, False), (hitbox.width, hitbox.height))
        self.jump_animation_left = pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_jump/1.png'),(hitbox.width, hitbox.height))
        self.fall_animation_right = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_fall/1.png'), True, False), (hitbox.width, hitbox.height))
        self.fall_animation_left = pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_crouch/1.png'),(hitbox.width, hitbox.height))
        self.cur_weapon = Item.DAGGER
        self.verticalForce = 0
        self.walkCount = 0
        self.isFalling = False
        self.isJumping = False
        self.isCrouched = False
        self.invince = False
        self.invince_time_ms = 500
        self.last_invince_timstep = 0
        self.last_attack_timestep = 0

    def handle_damage_interaction(self,interaction_msg: DamageMessage) -> None:
        if interaction_msg.target == (TargetType.PLAYER or TargetType.ALL_SPRITES):
            if interaction_msg.damage > 0:
                if((BackgroundEngine.get_current_time()-self.last_invince_timstep) > self.invince_time_ms):
                    self.invince = True
                    self.last_invince_timstep = BackgroundEngine.get_current_time()
                    print(self._health)
                    self._health -= interaction_msg.damage
            else:
                self._health -=interaction_msg.damage

    
    def handle_inventory_interaction(self,interaction_msg: InventoryMessage) -> None:
        if interaction_msg.target == (TargetType.PLAYER or TargetType.ALL_SPRITES):
            self.cur_weapon = interaction_msg.item

    def attack(self):
        if self.cur_weapon == Item.DAGGER:
            if BackgroundEngine.get_current_time()-self.last_attack_timestep>BasicAttack.get_attack_span():
                self.create_obj(BasicAttack(pygame.Rect(50, 200, 50, 80), self.get_pose_supplier(),TargetType.ENEMY,self.remove_obj))
                self.last_attack_timestep = BackgroundEngine.get_current_time()
    def return_current_image(self) -> pygame.Surface:

        if self.isFalling and self.direction < 0:
            return self.fall_animation_left
        elif self.isFalling:
            return self.fall_animation_right

        if self.isJumping and self.direction < 0:
            return self.jump_animation_left
        elif self.isJumping:
            return self.jump_animation_right

        if self.walkCount + 1 >= 17:
             self.walkCount = 0    
        if self.direction < 0:  
            self.walkCount += 0.5
            return self.walkLeft[int(self.walkCount//4) - 1]                
        elif self.direction > 0:
            self.walkCount += 0.5
            return self.walkRight[int(self.walkCount//4) - 1]
        else:
            self.walkCount = 0
    
        return self.image