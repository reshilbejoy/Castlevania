from abc import abstractmethod
from abc import ABC
from Abstract.Sprite import Sprite
from CompletedSprites.Platform import Platform
from Utils.signals import DamageMessage,InventoryMessage
from typing import List
import pygame
from Constants.window_constants import background_length

class DynamicSprite(Sprite,ABC):
    def __init__(self,terminal_vel_x:float, terminal_vel_y:float, images:List[pygame.Surface], hitbox:List[pygame.Rect], health:int, horizontal_force):
        super().__init__(images,hitbox)
        self._terminal_vel_x = terminal_vel_x
        self._terminal_vel_y = terminal_vel_y
        self._health = health
        self._horizontal_force = horizontal_force
        self._vertical_force = 0
        self.frictionForce = 0.2
        self.net_force = (abs(self.horizontalForce) - abs(self.frictionForce))
        self.starting_velocity_y = -15
        self.speed = 0
        self.left = False
        self.right = False
        self.current_velocity = 0 # y velocity
        self.collision_detection = False
        self.isJumping = False
        self.isFalling = False
        self.gravity = -self.starting_velocity_y * 0.05
    
    
    @abstractmethod
    def handle_damage_interaction(interaction_msg:InventoryMessage)->None:
        #handle damage
        pass

    @abstractmethod
    def handle_inventory_interaction(interaction_msg:DamageMessage)->None:
        #handle inventory
        pass

    def apply_force(self,all_platforms:List[Platform])->None:
        #Use all platforms list to move the sprite hitbox according to x and y forces TODO
        #print(self._hitbox.left)
        #print(self._hitbox.left, self.speed)
        if self.net_force > 0 and self._horizontal_force > 0 and self._hitbox.left <= background_length - self._hitbox.width:
            self.speeding_up()
            self._hitbox.left += self.speed
            self.left = False
            self.right = True
        elif self.net_force < 0 and self._horizontal_force < 0 and self._hitbox.left >= 0:
            self.speeding_up()
            self._hitbox.left -= self.speed
            self.left = True
            self.right = False

        if not self.speed <= 0 and self._horizontal_force == 0:
            self.slowing_down()
            if self.right:
                self._hitbox.left += self.speed
            else:
                self._hitbox.left -= self.speed

        if self.speed <= 0:
            self.left = False
            self.right = False
            self.net_force = 0
            self.speed = 0
        
        # vertical apply force
       
        #self.collision_detection = False
        self.canMove = True
        for platform in all_platforms:
            if self._hitbox.colliderect(platform._hitbox):
                
                if (self._hitbox.bottom >= platform._hitbox.top and self._hitbox.bottom <= platform._hitbox.bottom) and (self.current_velocity > 0):  # Collides from top
                    self.current_velocity = 0
                    self.collision_detection = True
                    self._hitbox.bottom = platform._hitbox.top + 1
                    self.isJumping = False
                    self.isFalling = False
                elif (self._hitbox.top <= platform._hitbox.bottom and self._hitbox.top >= platform._hitbox.top) and (self.current_velocity < 0):  # Collides from bottom (need to test)
                    print("g")
                    self.current_velocity = 0
                    self._hitbox.top = platform._hitbox.bottom
                #elif (self._hitbox.right >= platform._hitbox.left and self._hitbox.right <= platform._hitbox.right) and (self.right):  # Collides from right  (need to test)
                    #print('f')
                    #self.speed = 0
                    #self._hitbox.right = platform._hitbox.left
                #elif (self._hitbox.left <= platform._hitbox.right and self._hitbox.left >= platform._hitbox.left) and (self.left):  # Collides from left   (need to test)
                    #print('l')
                    #self.speed = 0
                    #self._hitbox.left = platform._hitbox.right

            #print(self._hitbox.colliderect(platform._hitbox))
        if not self.collision_detection: # collision_detection is true if there is a normal force
            self.current_velocity += self.gravity
            self._hitbox.top += self.current_velocity
            if self.current_velocity > self.starting_velocity_y:
                self.isFalling = True
            

    def change_force(self, x_force, y_force):
        self._horizontal_force = x_force
        self._verticalForce = y_force
        self.net_force = (abs(self._horizontal_force) - abs(self.frictionForce))
        if self._horizontal_force < 0:
            self.net_force *= -1            

    def speeding_up(self):
        if self.speed < self._terminal_vel_x:
            speed_val = self.speed + abs(self.net_force)
            self.speed = round(speed_val, 2)
    
    def slowing_down(self):
        if self.speed > 0:
            speed_val = self.speed - abs(self.frictionForce)
            self.speed = round(speed_val, 2)

    def jump(self):
        self.isJumping = True
        self.current_velocity = self.starting_velocity_y
        self._hitbox.top += self.current_velocity
        


