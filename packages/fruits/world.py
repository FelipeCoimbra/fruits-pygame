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


class World(ABC):

    def __init__(self) -> None:
        self._drawables = []
        self.fruits = []
        self.current_fruit = -1
        self.player = 0

    def register(self, game_object: GameObject) -> None:
        if game_object is not None:
            self._drawables.append(game_object)
            if type(game_object) == fruits.fruit.Fruit:
                self.fruits.append(game_object)

    @property
    def drawables(self) -> Iterable[GameObject]:
        return self._drawables

    def update_current_player(self):
        self.player = (self.player + 1) % 2

    def update_current_fruit(self):
        if self.current_fruit == -1:
            self.current_fruit = randint(0, len(self.fruits) - 1)
            self.player = self.fruits[self.current_fruit].player
            self.fruits[self.current_fruit].update_selected_status()
        elif len(self.fruits) >= 2:
            i = self.current_fruit
            k = 1
            while self.fruits[(i + k) % len(self.fruits)].player != self.player:
                k += 1

            self.fruits[i].update_selected_status()
            self.fruits[(i + k) % len(self.fruits)].update_selected_status()
            self.current_fruit = (i + k) % len(self.fruits)


class FruitsWorld(World):

    def __init__(self) -> None:
        super(FruitsWorld, self).__init__()

        # TODO: Create TerrainManager

        self._terrain = fruits.terrain.Terrain('terrain.png', (0, 0))

        fruits_to_register = [
            fruits.fruit.Fruit('tomato-sad.png', player=0, position=(200, 50)),
            fruits.fruit.Fruit('tomato-sad.png', player=0, position=(400, 50)),
            fruits.fruit.Fruit('tomato-sad.png', player=0, position=(600, 50)),
            fruits.fruit.Fruit('tomato-sad.png', player=0, position=(800, 50)),
            fruits.fruit.Fruit('tomato-sad.png', player=0, position=(1000, 50)),
            fruits.fruit.Fruit('watermellon-sad.png', player=1, position=(220, 50)),
            fruits.fruit.Fruit('watermellon-sad.png', player=1, position=(420, 50)),
            fruits.fruit.Fruit('watermellon-sad.png', player=1, position=(620, 50)),
            fruits.fruit.Fruit('watermellon-sad.png', player=1, position=(820, 50)),
            fruits.fruit.Fruit('watermellon-sad.png', player=1, position=(1020, 50))
        ]

        self.register(self._terrain)
        for fruit in fruits_to_register:
            self.register(fruit)

        self.update_current_fruit()

