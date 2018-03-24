from abc import ABC, abstractmethod
import fruits.background
import fruits.terrain
import fruits.shared_preferences as shared


class World(ABC):

    def __init__(self):
        pass


class FruitsWorld(World):

    def __init__(self):
        super(FruitsWorld, self).__init__()
        self.__terrain = fruits.terrain.Terrain('terrain.png', (0, 0))
