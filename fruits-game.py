import pygame
import fruits.game
from pygame import DOUBLEBUF, HWSURFACE
import fruits.shared_preferences as shared


def main():
    pygame.init()

    main_window = pygame.display.set_mode((shared.window_width, shared.window_height), DOUBLEBUF | HWSURFACE)
    pygame.display.set_caption('Fruits')

    fruits_game = fruits.game.FruitsGame(main_window)
    fruits_game.loop()
    fruits_game.quit()

    pygame.quit()


if __name__ == '__main__':
    main()
