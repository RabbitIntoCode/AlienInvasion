import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
#Checks and shows the implementatgion when pressing the mouse and keyboard events
def check_keydown(event,roc,sett,screen,bullets):
    if event.key == pygame.K_RIGHT:
        roc.move_right = True
    elif event.key == pygame.K_LEFT:
        roc.move_left = True
    elif  event.key == pygame.K_UP:
        roc.move_up = True
    elif event.key == pygame.K_DOWN:
        roc.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(sett,screen,roc,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup(event,roc):
    if event.key == pygame.K_RIGHT:
        roc.move_right = False
    elif event.key == pygame.K_LEFT:
        roc.move_left = False
    elif  event.key == pygame.K_UP:
        roc.move_up = False
    elif event.key == pygame.K_DOWN:
        roc.move_down = False
def check_event(roc,sett,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
             check_keydown(event,roc,sett,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event,roc)
def update_screen(roc,sett,screen,bullets,aliens):
    screen.fill(sett.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    roc.blitme()
    aliens.draw(screen)
    pygame.display.flip()
def fire_bullet(sett,screen,roc,bullets):
    # Create a new bullet and add it to the bullets group.
    new_bullet = Bullet(sett, screen, roc)
    bullets.add(new_bullet)
def update_bullets(sett,screen,aliens,roc,bullets):
#"""Update position of bullets and get rid of old bullets."""
 # Update bullet positions.
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(sett,screen,aliens,roc,bullets)
 # Check for any bullets that have hit aliens.
 # If so, get rid of the bullet and the alien.
def check_bullet_alien_collisions(sett,screen,aliens,roc,bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens)==0:
        #destroy existing bullets and create new fleet of aliens
        bullets.empty()
        alien_create_fleet(sett,screen,aliens,roc)
def get_number_rows(sett, roc_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (sett.screen_height -(3 * alien_height) - roc_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
def get_numberof_aliens(sett,ali_width):
    #determine number of aliens that fit in row
    avail_space = sett.screen_width - 2* ali_width
    num_ali = int(avail_space /(2* ali_width))
    return num_ali
def create_alien(sett,screen,aliens,row_number,i):
    alien = Alien(sett,screen)
    ali_width = alien.rect.width
    alien.x = ali_width + 2*ali_width*i
    alien.rect.x= alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
def alien_create_fleet(sett,screen,aliens,roc):
    #Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(sett,screen) 
    num_ali = get_numberof_aliens(sett, alien.rect.width)
    number_rows = get_number_rows(sett,roc.rect.height,alien.rect.height)
    # Create the first row of aliens.
    for row_number in range(number_rows):
        for i in range(num_ali):
            create_alien(sett,screen,aliens,row_number,i)
def check_fleet_edges(sett, aliens):
#Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            check_fleet_direc(sett, aliens)
            break
def ship_hit(sett,stats,screen,roc,aliens,bullets):
    if stats.roc_left>0:
        stats.roc_left -= 1
    # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
    #Create new fleet of aliens and center the ship again
        alien_create_fleet(sett,screen,aliens,roc)
        roc.center_roc()
    #pause
        sleep(0.5)
    else:
        stats.game_status =False
def update_alien(sett,stats,screen,roc,aliens,bullets):
 #Check if the fleet is at an edge,
 #and then update the postions of all aliens in the fleet.
    check_fleet_edges(sett, aliens)
    aliens.update()
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(sett, stats, screen, roc, aliens, bullets)
    #Look for alien ship colisions
    if pygame.sprite.spritecollideany(roc,aliens):
        ship_hit(sett,stats,screen,roc,aliens,bullets)
def check_fleet_direc(sett,aliens):
    #"""Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += sett.fleet_drop_speed
    sett.fleet_direction *= -1
def check_aliens_bottom(sett, stats, screen, roc, aliens, bullets):
#"""Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom: 
 # Treat this the same as if the ship got hit.
            ship_hit(sett, stats, screen, roc, aliens, bullets)
            break