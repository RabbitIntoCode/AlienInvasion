import pygame
from pygame.sprite import Sprite 
class Alien(Sprite):
    def __init__(self,sett,screen):
        super(Alien,self).__init__()
        self.sett = sett
        self.screen = screen
        self.image = pygame.image.load('Image/ALien1.bmp')
        self.rect =self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact position.
        self.x = float(self.rect.x)
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image,self.rect)   
    def check_edges(self):
       # ""Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """Move the alien right or left."""
        self.x += (self.sett.alien_speed_fac *self.sett.fleet_direction)
        self.rect.x = self.x
        
           