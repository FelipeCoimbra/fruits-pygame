from typing import Tuple

from fruits.game_object import GameObject


class Terrain(GameObject):
    def __init__(self, image: str, position: Tuple[int, int]) -> None:
        super(Terrain, self).__init__(image, position)
        self.image = self.image.copy().convert_alpha()

    def update(self, *args):
        pass

