import sys
import pygame as pg


def check_play_button(game, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        game.play()


def check_high_scores_button(game, high_scores_button, mouse_x, mouse_y):
    if high_scores_button.rect.collidepoint(mouse_x, mouse_y):
        pass


def check_events(game, play_button, high_scores_button):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            check_play_button(game, play_button, mouse_x, mouse_y)
            check_high_scores_button(game, high_scores_button, mouse_x, mouse_y)
