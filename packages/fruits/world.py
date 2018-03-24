from abc import ABC, abstractmethod
import fruits.background
import fruits.terrain
import fruits.shared_preferences as shared


class World(ABC):

    def __init__(self):
        self._drawables = []

    @abstractmethod
    def instantiate(self, game_object):
        pass

    def _register_drawable(self, drawable):
        self._drawables.append(drawable)

    def get_drawables(self):
        return self._drawables


class FruitsWorld(World):

    def __init__(self, terrain):
        super(FruitsWorld, self).__init__()
        self.__terrain = terrain
        self._register_drawable(terrain)

    def instantiate(self, game_object):
        pass

