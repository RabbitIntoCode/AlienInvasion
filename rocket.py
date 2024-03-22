import pygame
class Rocket():
    def __init__(self,sett,screen):
        self.screen = screen
        self.sett = sett
    # Load the ship image and get its rect.
        self.image = pygame.image.load('Image/Rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
 # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
    def update(self):
        if(self.move_right == True and self.rect.right<self.screen_rect.right):
            self.center += self.sett.speed_fac
        elif(self.move_left == True and self.rect.left>0):
            self.center -= self.sett.speed_fac
        elif(self.move_up == True):
            new_y = self.rect.y-self.sett.speed_fac
            self.rect.y = max(0, min(new_y, self.screen_rect.height - self.rect.height))
        elif(self.move_down == True):
            self.rect.y += self.sett.speed_fac
        self.rect.centerx = self.center
    def center_roc(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
    def blitme(self):
        self.screen.blit(self.image, self.rect)

        


