from abc import ABC
from typing import Iterable

import fruits.background
import fruits.terrain
import fruits.fruit
import fruits.shared_preferences as shared
from fruits.game_object import GameObject



class World(ABC):

    def __init__(self) -> None:
        self._drawables = []

    def register(self, game_object: GameObject) -> None:
        if game_object is not None:
            self._drawables.append(game_object)

    @property
    def drawables(self) -> Iterable[GameObject]:
        return self._drawables


class FruitsWorld(World):

    def __init__(self) -> None:
        super(FruitsWorld, self).__init__()
        # TODO: Create TerrainManager

        self.__terrain = fruits.terrain.Terrain('terrain.png',
                                                (shared.window_width/2, shared.window_height/2))
        fruit1 = fruits.fruit.Fruit('tomato-happy.png', position=(int(shared.window_width / 2),
                                                                  int(shared.window_height / 2)))
        # fruit2 = fruits.fruit.Fruit('watermellon-happy.png', position=(int(shared.window_width / 4),
        #                                                                int(shared.window_height / 4)))

        self.register(self.__terrain)
        self.register(fruit1)
        # self.register(fruit2)

