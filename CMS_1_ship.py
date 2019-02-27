import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen

        #load images
        self.image = pygame.image.load('Aircraft Material/my_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #let it in the low
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)