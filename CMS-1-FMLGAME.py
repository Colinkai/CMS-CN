import sys
import pygame

def run_game():
    pygame.init()
    #create interface
    screen= pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    #GAME STAR
    while True:
        #Monitor mouse and key board even
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Make the recently drawn screen visible
        pygame.display.flip()

run_game()


