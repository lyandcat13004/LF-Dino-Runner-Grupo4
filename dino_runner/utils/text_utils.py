from cgitb import text
import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)

    text = font.render('Points:' + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return text, text_rect

def get_centered_message(message, width=(SCREEN_WIDTH / 2), height=(SCREEN_HEIGHT / 2), font_size=22):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True,  BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect