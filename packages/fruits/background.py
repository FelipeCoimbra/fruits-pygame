from fruits.game_object import GameObject, GameObjectTransform
import fruits.shared_preferences as shared
from fruits.game_components import Mesh
from fruits.geometry.vector2d import Vector2D


class Background(GameObject):
    def __init__(self,
                 background_image_path: str,
                 position: Vector2D = Vector2D(0, 0)) -> None:
        super().__init__(GameObjectTransform(position))
        self.mesh = Mesh(self, image=background_image_path, width=shared.window_width, height=shared.window_height)

    def update(self, *args):
        pass

    def init(self):
        pass
