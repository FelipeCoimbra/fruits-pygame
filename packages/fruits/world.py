from abc import ABC, abstractmethod
import fruits.background
import fruits.terrain
import fruits.fruit
import fruits.shared_preferences as shared
from operator import itemgetter

from random import randint

class World(ABC):

    def __init__(self):
        self._drawables = []
        self.fruits = []
        self.current_fruit = -1

    def register(self, game_object):
        self._register_drawable(game_object)

    def _register_drawable(self, drawable):
        if drawable is not None:
            self._drawables.append(drawable)
            if type(drawable) == fruits.fruit.Fruit:
                self.fruits.append(drawable)

    def get_drawables(self):
        return self._drawables

    def update_current_fruit(self):
        if self.current_fruit == -1:
            self.current_fruit = randint(0, len(self.fruits) - 1)
            self.fruits[self.current_fruit].is_selected = True
            return

        if len(self.fruits) < 2:
            return

        current_fruit = self.fruits[self.current_fruit]
        self.fruits = sorted(self.fruits, key=lambda x: x.position[0])

        i = 0
        while self.fruits[i] != current_fruit:
            i += 1

        self.fruits[i].is_selected = False
        self.fruits[(i + 1) % len(self.fruits)].is_selected = True
        self.current_fruit = (i + 1) % len(self.fruits)


class FruitsWorld(World):

    def __init__(self) -> None:
        super(FruitsWorld, self).__init__()
        # TODO: Create TerrainManager

        self.__terrain = fruits.terrain.Terrain('terrain.png',
                                                (shared.window_width/2, shared.window_height/2))

        fruit1 = fruits.fruit.Fruit('tomato-smile.png', position=(randint(50,shared.window_width - 50),
                                                                  randint(50,shared.window_height - 50)))
        fruit2 = fruits.fruit.Fruit('watermellon-smile.png', position=(randint(50,shared.window_width - 50),
                                                                       randint(50,shared.window_height - 50)))
        fruit3 = fruits.fruit.Fruit('watermellon-smile.png', position=(randint(50,shared.window_width - 50),
                                                                       randint(50,shared.window_height - 50)))
        fruit4 = fruits.fruit.Fruit('watermellon-smile.png', position=(randint(50,shared.window_width - 50),
                                                                       randint(50,shared.window_height - 50)))

        self.register(self.__terrain)
        self.register(fruit1)
        self.register(fruit2)
        self.register(fruit3)
        self.register(fruit4)

        self.update_current_fruit()

