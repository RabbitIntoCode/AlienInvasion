import pygame
from settings import Settings
from rocket import Rocket
from pygame.sprite import Group
from game_stats import Game_stats
import game_fns as gf
def run_game():
    #TO start the pygame package 
    pygame.init()
    #To call the settings class into this homeAI
    sett = Settings()
    # Create an instance to store game statistics.
    stats = Game_stats(sett)
    #To create an empty window with specific dimensions
    screen = pygame.display.set_mode((sett.screen_width,sett.screen_height))
    roc = Rocket(sett,screen)
    bullets =Group() 
    aliens = Group()
    pygame.display.set_caption("Alien Invasion")
    gf.alien_create_fleet(sett,screen,aliens,roc)
    while True:
        # To access each and every action of user
        gf.check_event(roc,sett,screen,bullets)
        if stats.game_status:
            roc.update()
            gf.update_bullets(sett,screen,aliens,roc,bullets)
            gf.update_alien(sett,stats,screen,roc,aliens,bullets)
        gf.update_screen(roc,sett,screen,bullets,aliens)
run_game()
 