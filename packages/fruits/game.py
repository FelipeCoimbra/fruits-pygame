import pygame


class FruitsGame(object):
    def __init__(self, main_window) -> None:
        self.main_window = main_window

    def loop(self) -> None:
        clock = pygame.time.Clock()

        while True:
            delta = clock.tick(60)

            for event in pygame.event.get():
                if event == pygame.QUIT:
                    return

            pygame.display.update()

    def quit(self) -> None:
        pass
