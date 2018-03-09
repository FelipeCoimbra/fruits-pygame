import pygame
from game.FruitsGame import FruitsGame

pygame.init()

main_window = pygame.display.set_mode()

FruitsGame(main_window).run()

