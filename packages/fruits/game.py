import pygame
import fruits.input
import fruits.control_room
from fruits.background import Background
from fruits.terrain import Terrain


class FruitsGame(object):
    def __init__(self, main_window) -> None:
        self.main_window = main_window
        self.__input_handler = fruits.input.InputHandler()
        self.__scene_manager = fruits.control_room.SceneManager()

    def loop(self) -> None:
        clock = pygame.time.Clock()
        x, y = self.main_window.get_size()
        background = Background('blue-background.png', (x, y))
        terrain = Terrain('terrain.png', (x/2, y/2))

        gameScreen = pygame.display.get_surface()

        while True:
            delta = clock.tick(60)

            commands = (self.__input_handler
                            .events_to_commands(pygame.event.get()))

            self.__scene_manager.manage(commands)


            background.draw_on(gameScreen)
            terrain.draw_on(gameScreen)


            pygame.display.update()

    def quit(self) -> None:
        pass
