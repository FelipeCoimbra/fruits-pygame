from fruits.controllers.controller import Controller
from fruits.game_entity import GameEntity
from fruits.command import Command
from fruits.geometry.vector2d import Vector2D
import pygame


class TerrainController(Controller):
    listening_events = [
        Command.MOUSE_LEFT_DOWN
    ]

    def __init__(self, terrain_entity: 'Terrain'):
        super().__init__(terrain_entity)

    def receive(self, command: str) -> None:
        # if command == Command.MOUSE_LEFT_DOWN:
        #     self.entity.destroy(Vector2D.from_cardinal_tuple(pygame.mouse.get_pos()))
        pass
