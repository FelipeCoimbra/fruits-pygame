from fruits.game_entity import GameEntity
from fruits.controllers.menu_controller import MenuController
from typing import Tuple
from fruits.controllers.fruit_controller import FruitController
from fruits.game_object import GameObject
import fruits.shared_preferences as shared
from fruits.game_components import Mesh


class Menu(GameEntity):

    # Menu status

    def __init__(self, scene):
        super(Menu, self).__init__()
        self.__scene = scene
        self.attach_controller(MenuController(self))

    def interrupt(self):
        # Ends match suddenly
        self.__scene.stop()



class Option(GameObject):
    def __init__(self,
                 image: str,
                 position: Tuple[int, int] = (0, 0)) -> None:
        super(GameObject, self).__init__()

        self.attach_controller(FruitController(self))
        self.mesh = Mesh(image=image, position=position,
                         width=shared.character_width, height=shared.character_height)


    def init(self) -> None:
        pass

    def update(self) -> None:
        pass
