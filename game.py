import pygame as pg
from settings import Settings
import game_functions as gf
from pacman import Pacman
from button import Button


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pac-Man Portal")

        self.image = pg.image.load('images/map_empty.bmp')
        self.rect = (0, 48)
        # self.rect = self.map.get_rect()

        self.pacman = Pacman(game=self, screen=self.screen, settings=self.settings)
        self.play_button = Button(screen=self.screen, top=400, width=240, height=50, msg="PLAY GAME")
        self.high_scores_button = Button(screen=self.screen, top=460, width=240, height=50, msg="HIGH SCORES")

    def main_menu(self):
        while True:
            gf.check_events(game=self, play_button=self.play_button, high_scores_button=self.high_scores_button)
            self.screen.fill(self.settings.bg_color)
            self.play_button.update()
            self.high_scores_button.update()
            pg.display.flip()

    def reset(self):
        pass

    def game_over(self):
        pass

    def play(self):
        while True:
            gf.check_events(game=self, play_button=self.play_button, high_scores_button=self.high_scores_button)
            self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.image, self.rect)
            self.pacman.update()
            pg.display.flip()


def main():
    window = pg.display.set_mode((1200, 800))
    pg.display.set_caption("PacMan")
    black = (0, 0, 0)
    end_screen = False
    pg.mixer.init()

    window.fill(black)
    imp = pg.image.load("images/start.png")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_screen = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                end_screen = True

    g = Game()
    g.main_menu()

    window.blit(imp, (0,0))
    pg.display.flip()


if __name__ == '__main__':
    main()
