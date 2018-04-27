from typing import Iterator

import pygame
import fruits.command
from fruits.events.explosion import ExplosionEvent, ToggleTeamEvent
from fruits.explosion_effect import ExplosionEffectEvent


class InputHandler:
    def __init__(self) -> None:
        self.__command_map = fruits.command.commands

    def events_to_commands(self, events) -> Iterator:
        for event in events:
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                command = self.__command_map.get((event.type, event.key))
                if not command and event.type == pygame.KEYDOWN:
                    command = self.__command_map.get(event.key)

            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                left, middle, right = pygame.mouse.get_pressed()
                posx, posy = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("mouse at ", posx, posy)

                if left:
                    mouse_button = fruits.command.MouseButtons.LEFT
                elif middle:
                    mouse_button = fruits.command.MouseButtons.RIGHT
                elif right:
                    mouse_button = fruits.command.MouseButtons.MIDDLE
                else:
                    mouse_button = None

                command = self.__command_map.get((event.type, mouse_button))
            elif event.type == pygame.USEREVENT:
                if event.event_class == ExplosionEvent:
                    command = event.event_class(event.position, event.bomb)
                elif event.event_class == ToggleTeamEvent:
                    command = event.event_class()
                elif event.event_class == ExplosionEffectEvent:
                    command = event.event_class(event.entity)
            else:
                command = self.__command_map.get(event.type)

            if command is not None:
                yield command
