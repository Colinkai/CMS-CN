import sys
import pygame
from CMS_1_settings import Settings
from CMS_1_ship import Ship
import CMS_1_game_functions as gf
def run_game():
    pygame.init()
    #create interface
    ai_settingts = Settings()
    screen= pygame.display.set_mode((ai_settingts.screen_width,ai_settingts.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Creat a Aircraft material
    ship = Ship(screen)
    #GAME STAR
    while True:
        #Monitor mouse and key board even
        gf.check_events()


        screen.fill(ai_settingts.bg_color)
        screen.blit(ai_settingts.background,(0,0))
        ship.blitme()
        #Make the recently drawn screen visible
        pygame.display.flip()

run_game()


