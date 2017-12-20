import pygame
from ship import Ship
from settings import Setting
import sys

# def run_game():
#     pygame.init()
#     bg_color = (230, 230, 230)
#     screen=pygame.display.set_mode((1200,800))
#     caption=pygame.display.set_caption('Alien')
#
#     while True:
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 sys.exit()
# run_game()


def run_game():
    pygame.init()
    ai_setting=Setting()
    screen= pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('Alien')
    ship=Ship(screen)
    while True:
        screen.fill(ai_setting.bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()