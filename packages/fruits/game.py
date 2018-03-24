import pygame
import fruits.input
import fruits.control_room
from fruits.background import Background
from fruits.terrain import Terrain


class FruitsGame(object):
    def __init__(self, main_window) -> None:
        self.main_window = main_window
        self.__input_handler = fruits.input.InputHandler()
        self.__control_room = fruits.control_room.ControlRoom()

    def loop(self) -> None:
        clock = pygame.time.Clock()
        x, y = self.main_window.get_size()
        background = Background('blue-background.png', (x, y))
        terrain = Terrain('terrain.png', (0, 0))

        gameScreen = pygame.display.get_surface()

        while True:
            delta = clock.tick(60)

            if len(pygame.event.get(pygame.QUIT)) > 0:
                    return

            self.__input_handler.update_user_command(pygame.event.get())

            # self.__control_room.manage(self.__input_handler.get_user_commands())

            '''
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("Space bar pressed down.")
                    elif event.key == pygame.K_ESCAPE:
                        print("Escape key pressed down.")
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        print("Space bar released.")
                    elif event.key == pygame.K_ESCAPE:
                        print("Escape key released.")'''

            background.draw_on(gameScreen)
            terrain.draw_on(gameScreen)

            pygame.display.update()

    def quit(self) -> None:
        pass
