from abc import ABC
from typing import Iterable, List, Tuple
from random import randint
from fruits.game_object import GameObject
import fruits.background
import fruits.terrain
import fruits.fruit
from fruits.fruit import Fruit
import pygame
from fruits.menu import Option
import fruits.shared_preferences as shared
# from numpy import hypot
from math import hypot
from fruits.geometry.vector2d import Vector2D
from fruits.game_event import EventHandler


class World(ABC):

    def __init__(self, event_handler=None) -> None:
        self._event_handler = event_handler
        self._drawables: List[GameObject] = []
        self.fruits: List[fruits.fruit.Fruit] = []
        self.current_fruit = -1
        self.current_player = -1

    def register(self, game_object: GameObject) -> None:
        if game_object is not None:
            self._drawables.append(game_object)
            if isinstance(game_object, fruits.fruit.Fruit):
                self.fruits.append(game_object)

    @property
    def drawables(self) -> Iterable[GameObject]:
        return self._drawables

    def update_current_player(self):
        self.current_player = (self.current_player + 1) % 2
        print(f"now team {self.current_player}")
        self.update_current_fruit()

    def update_current_fruit(self):
        if self.current_fruit == -1:
            self.current_fruit = randint(0, len(self.fruits) - 1)
            self.current_player = self.fruits[self.current_fruit].player
            self.fruits[self.current_fruit].toggle_selected()
        elif len(self.fruits) >= 2:
            i = self.current_fruit
            k = 1
            while self.fruits[(i + k) % len(self.fruits)].player != self.current_player:
                k += 1

            self.fruits[i].toggle_selected()
            self.fruits[(i + k) % len(self.fruits)].toggle_selected()
            self.current_fruit = (i + k) % len(self.fruits)

    def damage_fruits(self, explosion_position: Vector2D) -> None:
        e_x, e_y = explosion_position.x, explosion_position.y
        explosion_radius = shared.character_width * 5.0
        for fruit in self.fruits:
            f_x, f_y = fruit.position.x, fruit.position.y
            distance = hypot(abs(e_x - f_x), abs(e_y - f_y))
            if distance < explosion_radius:
                fruit.stamina -= 10 + .6 * (explosion_radius - distance)
                if fruit.stamina <= 0:
                    self.fruits.remove(fruit)


class FruitsWorld(World):

    def __init__(self, event_handler: EventHandler=None) -> None:
        super().__init__(event_handler)

        # TODO: Create TerrainManager

        self._terrain = fruits.terrain.Terrain('terrain.png', Vector2D(0, 0))
        if self._event_handler is not None:
            self._event_handler.subscribe_entity(self._terrain)

        self._bomb = None

        to_register = [
            self._terrain,
            Fruit('tomato-smile.png', player=0, position=Vector2D(200, 50)),
            Fruit('tomato-smile.png', player=0, position=Vector2D(400, 50)),
            Fruit('tomato-smile.png', player=0, position=Vector2D(600, 50)),
            Fruit('tomato-smile.png', player=0, position=Vector2D(800, 50)),
            Fruit('tomato-smile.png', player=0, position=Vector2D(1000, 50)),
            Fruit('watermellon-smile.png', player=1, position=Vector2D(220, 50)),
            Fruit('watermellon-smile.png', player=1, position=Vector2D(420, 50)),
            Fruit('watermellon-smile.png', player=1, position=Vector2D(620, 50)),
            Fruit('watermellon-smile.png', player=1, position=Vector2D(820, 50)),
            Fruit('watermellon-smile.png', player=1, position=Vector2D(1020, 50)),
        ]

        for fruit in to_register:
            self.register(fruit)

        self.update_current_player()

    @property
    def terrain(self):
        return self._terrain

    @property
    def bomb(self):
        return self._bomb

    @bomb.setter
    def bomb(self, val):
        self._bomb = val


class Menu(World):

    def __init__(self, event_handler=None) -> None:
        super().__init__(event_handler)
        #
        #
        #
        # to_register = [
        #     Option(label=pygame.font.Font("fonts/Minecrafter.Alt.ttf", 50, bold=(self._world.current_player == 0)).
        #            render("PLAY", 1, (255, 255, 0)),
        #            position=(int(shared.window_width / 2) - 50, int(shared.window_height / 3) + 60)),
        #     Option(label=pygame.font.Font("fonts/Minecrafter.Alt.ttf", 50, bold=(self._world.current_player == 0)).
        #            render("QUIT", 1, (0, 0, 0)),
        #            position=(int(shared.window_width / 2) - 50, int(shared.window_height / 3) + 120))
        # ]
        #
        # for el in to_register:
        #     self.register(fruit)
