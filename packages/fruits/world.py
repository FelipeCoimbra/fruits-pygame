from abc import ABC, abstractmethod
import fruits.background
import fruits.terrain
import fruits.shared_preferences as shared


class World(ABC):

    def __init__(self):
        self._drawables = []

    def register(self, game_object):
        self._register_drawable(game_object)

    def _register_drawable(self, drawable):
        if drawable is not None:
            self._drawables.append(drawable)

    def get_drawables(self):
        return self._drawables


class FruitsWorld(World):

    def __init__(self) -> None:
        super(FruitsWorld, self).__init__()
        # TODO: Create TerrainManager
        self.__terrain = fruits.terrain.Terrain('terrain.png',
                                                (shared.window_width/2, shared.window_height/2))
        self.register(self.__terrain)


