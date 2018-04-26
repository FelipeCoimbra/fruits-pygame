import abc

from fruits.game_entity import GameEntity


class GameObject(GameEntity, abc.ABC):
    def __init__(self) -> None:
        GameEntity.__init__(self)

    @abc.abstractmethod
    def init(self) -> None:
        pass

    @abc.abstractmethod
    def update(self, *args) -> None:
        pass
