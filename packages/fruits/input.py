from typing import Iterator

import pygame
import fruits.command


class InputHandler:
    def __init__(self) -> None:
        self.__command_map = fruits.command.commands

    def events_to_commands(self, events) -> Iterator:
        for event in events:
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                command = self.__command_map.get((event.type, event.key))
            else:
                command = self.__command_map.get(event.type)

            if command is not None:
                yield command
