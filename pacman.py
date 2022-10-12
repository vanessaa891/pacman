import pygame as pg
from pygame.sprite import Sprite
from vector import Vector


class Pacman(Sprite):
    def __init__(self, game, settings, screen):
        super().__init__()
        self.game = game
        self.screen = screen
        self.settings = settings
        self.image = pg.image.load('images/pacman_2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.posn = self.center_pacman()

    def center_pacman(self):
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom
        self.rect.left = 212
        self.rect.top = 410
        return Vector(self.rect.left, self.rect.top)

    def update(self):
        self.draw()

    def draw(self):
        self.screen.blit(self.image, self.rect)
