from abc import ABC
import abc
from typing import Iterable
from random import randint
from fruits.game_object import GameObject
import fruits.background
import fruits.terrain
import fruits.fruit
import fruits.shared_preferences as shared
import pygame
from fruits.geometry.vector2d import Vector2D


class World(ABC):

    def __init__(self) -> None:
        self._drawables = []
        self.fruits = []
        self.current_fruit = -1

    def register(self, game_object: GameObject) -> None:
        if game_object is not None:
            self._drawables.append(game_object)
            if type(game_object) == fruits.fruit.Fruit:
                self.fruits.append(game_object)

    @property
    def drawables(self) -> Iterable[GameObject]:
        return self._drawables


class FruitsWorld(World):

    def __init__(self) -> None:
        super(FruitsWorld, self).__init__()

        # TODO: Create TerrainManager

        self._terrain = fruits.terrain.Terrain('terrain.png', Vector2D(0, 0))
        fruit1 = fruits.fruit.Fruit(image='tomato-sad.png', position=Vector2D(200, 50))
        fruit2 = fruits.fruit.Fruit(image='tomato-sad.png', position=Vector2D(400, 50))
        fruit3 = fruits.fruit.Fruit(image='tomato-sad.png', position=Vector2D(600, 50))
        fruit4 = fruits.fruit.Fruit(image='tomato-sad.png', position=Vector2D(800, 50))
        fruit5 = fruits.fruit.Fruit(image='tomato-sad.png', position=Vector2D(1000, 50))
        self.register(self._terrain)
        self.register(fruit1)
        self.register(fruit2)
        self.register(fruit3)
        self.register(fruit4)
        self.register(fruit5)

        self.current_fruit = -1
        self.update_current_fruit()

    @property
    def terrain(self):
        return self._terrain

    def update_current_fruit(self):
        if self.current_fruit == -1:
            self.current_fruit = randint(0, len(self.fruits) - 1)
            self.fruits[self.current_fruit].toggle_selected()
            return

        if len(self.fruits) < 2:
            return

        i = -1
        while i != self.current_fruit:
            i = randint(0, len(self.fruits) - 1)

        self.fruits[i].toggle_selected()
        self.fruits[(i + 1) % len(self.fruits)].toggle_selected()
        self.current_fruit = (i + 1) % len(self.fruits)
