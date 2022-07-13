import pygame
from pygame.sprite import Sprite

class Gun(Sprite):

    def __init__(self, screen):

        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def updatepos(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx +=2

        if self.mleft and self.rect.left > 0:
            self.rect.centerx -=2
    def create_gun(self):
        """размещение пушки по центру внизу экрана"""
        self.center = self.screen_rect.centerx