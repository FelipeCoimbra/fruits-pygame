import pygame
import fruits.command

class InputHandler:

    def __init__(self):
        self.__current_commands = {}
        self.__command_map = {}
        self.__init_default_commandmap()

    def __init_default_commandmap(self):
        self.__command_map[pygame.K_UP] = fruits.command.Command.UP
        self.__command_map[pygame.K_DOWN] = fruits.command.Command.UP
        self.__command_map[pygame.K_LEFT] = fruits.command.Command.LEFT
        self.__command_map[pygame.K_RIGHT] = fruits.command.Command.RIGHT
        self.__command_map[pygame.K_SPACE] = fruits.command.Command.SPACE
        self.__command_map[pygame.K_ESCAPE] = fruits.command.Command.ESCAPE

    def get_user_commands(self):
        return self.__current_commands

    def update_user_command(self, input_list):
        new_commands = {}
        for pyinput in input_list:
            if pyinput.type != pygame.KEYDOWN and pyinput.type != pygame.KEYUP:
                continue

            action = self.__command_map.get(pyinput.key)
            command = self.__current_commands.get(action)
            if pyinput.type == pygame.KEYDOWN:
                new_commands[action] = fruits.command.Command(action)

                if command is None:
                    self.__current_commands[action] = fruits.command.Command(action)
                else:
                    command.increment_count()
            elif command is not None:
                del self.__current_commands[action]
