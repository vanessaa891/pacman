import pygame as pg
from settings import Settings
import game_functions as gf
from pacman import Pacman


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pac-Man Portal")
        self.font = pg.font.SysFont(None, 30)

        self.image = pg.image.load('images/map_empty.bmp')
        self.rect = (0, 48)
        # self.rect = self.map.get_rect()

        self.pacman = Pacman(game=self, screen=self.screen, settings=self.settings)

    def reset(self):
        pass

    def game_over(self):
        pass

    def play(self):
        while True:
            gf.check_events()
            self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.image, self.rect)
            self.pacman.update()
            pg.display.flip()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
