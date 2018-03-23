import pygame
import fruits.input
import fruits.control_room

class FruitsGame(object):
    def __init__(self, main_window) -> None:
        self.main_window = main_window
        self.__input_handler = fruits.input.InputHandler()
        self.__control_room = fruits.control_room.ControlRoom()

    def loop(self) -> None:
        clock = pygame.time.Clock()

        while True:
            delta = clock.tick(60)

            quit_events = pygame.event.get(pygame.QUIT)
            if len(quit_events) > 0:
                    return

            self.__input_handler.update_user_command(pygame.event.get())

            self.__control_room.manage(self.__input_handler.get_user_commands())

            self.__drawer.control

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

            pygame.display.update()

    def quit(self) -> None:
        pass
