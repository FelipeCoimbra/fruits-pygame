import pygame
import fruits.game


WIDTH = 800
HEIGHT = 600


def main():
    pygame.init()

    main_window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Fruits')

    fruits_game = fruits.game.FruitsGame(main_window)
    fruits_game.loop()
    fruits_game.quit()

    pygame.quit()


if __name__ == '__main__':
    main()
