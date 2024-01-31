from typing import Callable, List, TypedDict
import pygame
from Abstract.Player import Player
from Abstract.Interaction import Interactable
from CompletedSprites.Interactables.BasicAttack import BasicAttack
from Utils.signals import DamageMessage, InventoryMessage, Item, TargetType
from CompletedSprites.Interactables.CandyCane import CandyCane

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
        
        self.attackWalkRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_attack_walk/1.png'), True, False), (hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_attack_walk/2.png'), True, False), (hitbox.width + 20, hitbox.height)),
                            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_attack_walk/3.png'), True, False), (hitbox.width + 20, hitbox.height))]
        
        self.attackWalkLeft = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_attack_walk/1.png'),(hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_attack_walk/2.png'),(hitbox.width + 20, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_attack_walk/3.png'),(hitbox.width + 20, hitbox.height))]
        
        self.attackJumpRight = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_attack_jump/1.png'), True, False), (hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_attack_jump/2.png'), True, False), (hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_attack_jump/3.png'), True, False), (hitbox.width, hitbox.height))]
        
        self.attackJumpLeft = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_attack_jump/1.png'),(hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_attack_jump/2.png'),(hitbox.width, hitbox.height)),
                            pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_attack_jump/3.png'),(hitbox.width, hitbox.height))]
    

        self.image_right = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/1.png'), True, False), (hitbox.width, hitbox.height))
        self.image_left = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_walk/1.png'), False, False), (hitbox.width, hitbox.height))
        self.jump_animation_right = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_jump/1.png'), True, False), (hitbox.width, hitbox.height))
        self.jump_animation_left = pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_jump/1.png'),(hitbox.width, hitbox.height))
        self.fall_animation_right = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_fall/1.png'), True, False), (hitbox.width, hitbox.height))
        self.fall_animation_left = pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_fall/1.png'),(hitbox.width, hitbox.height))
        self.crouch_animation_right = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/Sprites/Player_crouch/1.png'), True, False), (hitbox.width, hitbox.height))
        self.crouch_animation_left = pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_crouch/1.png'),(hitbox.width, hitbox.height))

        self.cur_weapon = Item.WHIP
        self.state_dict = {}
        self.verticalForce = 0
        self.walkCount = 0
        self.isFalling = False
        self.isJumping = False
        self.isCrouched = False
        self.isMoving = False
        self.invince = False
        self.isAttacking = False
        self.invince_time_ms = 500
        self.last_invince_timstep = 0
        self.last_attack_timestep = 0
        self.player_jump_attack_count = 0
        self.player_walk_attack_count = 0
        self.last_attack_animation_timestep= 0
        self.images_hit = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_hurt/1.png'), (hitbox.width, hitbox.height))]
        self._death = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_death/1.png'), (50, 50)), 
                       pygame.transform.scale(pygame.image.load('Assets/Sprites/Player_death/2.png'), (80, 30))]

    def handle_damage_interaction(self,interaction_msg: DamageMessage) -> None:
        if interaction_msg.target == (TargetType.PLAYER or TargetType.ALL_SPRITES) and not self._hit:
            print("hit")
            if interaction_msg.damage > 0:
                if((BackgroundEngine.get_current_time()-self.last_invince_timstep) > self.invince_time_ms):
                    self.invince = True
                    self.last_invince_timstep = BackgroundEngine.get_current_time()
                    # print(self._health)
                else:
                    self._health -=interaction_msg.damage
                    self._hit = True
                self._hit_time = BackgroundEngine.get_current_time()
            if self._health <= 0 and self.timestamp == 0:
                self.timestamp = BackgroundEngine.get_current_time()

    
    def handle_inventory_interaction(self,interaction_msg: InventoryMessage) -> None:
        if interaction_msg.target == (TargetType.PLAYER or TargetType.ALL_SPRITES):
            self.cur_weapon = interaction_msg.item

    def attack(self):
        
        if self.cur_weapon == Item.WHIP:
            if not self.isAttacking:
                self.create_obj(BasicAttack(pygame.Rect(0, 0, 160, 100), self.get_pose_supplier(),TargetType.ENEMY,self.remove_obj))
                self.last_attack_timestep = BackgroundEngine.get_current_time()
                self.last_attack_animation_timestep = BackgroundEngine.get_current_time()
        elif self.cur_weapon == Item.DAGGER:
                di = -1
                if self.direction >= 0:
                    di = 1
                self.create_obj(CandyCane(pygame.Rect(50, 200, 50, 30), self.get_pose_supplier(),TargetType.ENEMY,self.remove_obj,di))

    def init_obj(self) -> None:
        pass

    def return_current_image(self) -> pygame.Surface:
        # print(self._health)

        #player is not attacking
        if self._health > 0:
            if self.check_hit():
                return self.images_hit[0]
            if self.isCrouched:
                return self.crouch_animation_right
            self.isAttacking = not BackgroundEngine.get_current_time() - self.last_attack_timestep>BasicAttack.get_attack_span()
            if self.isFalling and self.direction < 0:
                return self.fall_animation_left
            elif self.isFalling:
                return self.fall_animation_right
            if self.isAttacking:
                if(BackgroundEngine.get_current_time() - self.last_attack_animation_timestep < 0.3*BasicAttack.get_attack_span()):
                    if self.direction>=0:
                        if self.isJumping or self.isFalling:
                            return self.attackJumpRight[0]
                        else:
                            return self.attackWalkRight[0]
                    else:
                        if self.isJumping or self.isFalling:
                            return self.attackJumpLeft[0]
                        else:
                            return self.attackWalkLeft[0]
                    
                if(BackgroundEngine.get_current_time() - self.last_attack_animation_timestep < 0.6*(BasicAttack.get_attack_span())):
                    if self.direction>=0:
                        if self.isJumping or self.isFalling:
                            return self.attackJumpRight[1]
                        else:
                            return self.attackWalkRight[1]
                    else:
                        if self.isJumping or self.isFalling:
                            return self.attackJumpLeft[1]
                        else:
                            return self.attackWalkLeft[1]
                        
                if(BackgroundEngine.get_current_time() - self.last_attack_animation_timestep <= (BasicAttack.get_attack_span())):
                    if self.direction>=0:
                        if self.isJumping or self.isFalling:
                            return self.attackJumpRight[2]
                        else:
                            return self.attackWalkRight[2]
                    else:
                        if self.isJumping or self.isFalling:
                            return self.attackJumpLeft[2]
                        else:
                            return self.attackWalkLeft[2]

            if self.isJumping and self.direction < 0:
                return self.jump_animation_left

            elif self.isJumping:
                return self.jump_animation_right

            if self.walkCount + 1 >= 17:
                self.walkCount = 0  
            if self.isMoving:  
                if self.direction < 0:  
                    self.walkCount += 0.1
                    return self.walkLeft[int(self.walkCount//4) - 1]                
                elif self.direction > 0:
                    self.walkCount += 0.1
                    return self.walkRight[int(self.walkCount//4) - 1]
            else:
                if self.direction < 0:  
                    return self.image_left           
                elif self.direction > 0:
                    self.walkCount += 0.1
                    return self.image_right
            
            return self.image_right
        if BackgroundEngine.get_current_time() - self.timestamp <= 2000:
            return self._death[0]
        else:
            if BackgroundEngine.get_current_time() - self.timestamp > 4000:
                self._dead = True
            return self._death[1]


    def check_hit(self):
        if self._hit:
            print(BackgroundEngine.get_current_time()-self._hit_time)
            if BackgroundEngine.get_current_time()-self._hit_time >= 500:
                self._hit = False
        return self._hit