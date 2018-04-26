import pygame
import fruits.input
import fruits.scene_manager
from fruits.background import Background
from fruits.terrain import Terrain


class FruitsGame(object):
    def __init__(self, main_window) -> None:
        self.main_window = main_window
        self.__input_handler = fruits.input.InputHandler()
        self.__scene_manager = fruits.scene_manager.SceneManager()

    def loop(self) -> None:
        clock = pygame.time.Clock()

        game_screen = pygame.display.get_surface()

        while True:
            clock.tick(60)

            commands = (self.__input_handler
                            .events_to_commands(pygame.event.get()))
            manager_alive = self.__scene_manager.manage(commands)
            if not manager_alive:
                return

            self.__scene_manager.draw_scene(game_screen)

            pygame.display.update()

    def quit(self) -> None:
        pass
