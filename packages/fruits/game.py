import pygame
import fruits.input
import fruits.control_room

class FruitsGame(object):
    def __init__(self, main_window) -> None:
        self.main_window = main_window
        self.__input_handler = fruits.input.InputHandler()
        self.__scene_manager = fruits.control_room.SceneManager()

    def loop(self) -> None:
        clock = pygame.time.Clock()

        while True:
            delta = clock.tick(60)

            quit_events = pygame.event.get(pygame.QUIT)
            if len(quit_events) > 0:
                    return

            self.__input_handler.update_by_user_input(pygame.event.get())

            self.__scene_manager.manage(self.__input_handler.get_user_commands())

            pygame.display.update()

    def quit(self) -> None:
        pass
