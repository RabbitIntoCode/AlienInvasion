from typing import Any
import pygame
from pygame.sprite import Group, Sprite

class Bullet(Sprite):
    def __init__(self,sett,screen,roc):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,sett.bullet_width,sett.bullet_height)
        self.rect.centerx = roc.rect.centerx
        self.rect.top = roc.rect.top
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.color = sett.bullet_color
        self.sp_fac = sett.bullet_speed_fac
    def update(self):
        #Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.sp_fac
        # Update the rect position
        self.rect.y =self.y
    def draw_bullet(self):
 #"""Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


