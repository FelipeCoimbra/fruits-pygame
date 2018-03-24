import typing
import pygame
import fruits.command

class InputHandler:

    def __init__(self) -> None:
        self.__current_commands = {}
        self.__command_map = {}
        self.__init_default_commandmap()
        self.__outdated = False

    def __init_default_commandmap(self) -> None:
        self.__command_map[pygame.K_UP] = fruits.command.Command.UP
        self.__command_map[pygame.K_DOWN] = fruits.command.Command.UP
        self.__command_map[pygame.K_LEFT] = fruits.command.Command.LEFT
        self.__command_map[pygame.K_RIGHT] = fruits.command.Command.RIGHT
        self.__command_map[pygame.K_SPACE] = fruits.command.Command.SPACE
        self.__command_map[pygame.K_ESCAPE] = fruits.command.Command.ESCAPE

    def get_user_commands(self) -> typing.Dict[int, fruits.command.Command]:
        return self.__current_commands

    def update_by_user_input(self, input_list) -> None:
        self.__update_before_input()

        for pyinput in input_list:
            if pyinput.type != pygame.KEYDOWN and pyinput.type != pygame.KEYUP:
                continue

            action = self.__command_map.get(pyinput.key)
            command = self.__current_commands.get(action)
            if pyinput.type == pygame.KEYDOWN and command is None:
                    self.__current_commands[action] = fruits.command.Command(action)
            elif pyinput.type == pygame.KEYUP and command is not None:
                self.__current_commands.pop(action)

        self.__outdated = True

    def __update_before_input(self):
        if not self.__outdated:
            return

        for command in self.__current_commands.values():
            command.increment_count()

        self.__outdated = False
