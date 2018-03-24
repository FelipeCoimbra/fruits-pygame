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
            delta = clock.tick(60)

            if len(pygame.event.get(pygame.QUIT)) > 0:
                    return

            self.__input_handler.update_by_user_input(pygame.event.get())

            self.__scene_manager.manage(self.__input_handler.user_commands)

            self.__scene_manager.draw_scene(game_screen)

            pygame.display.update()

    def quit(self) -> None:
        pass
