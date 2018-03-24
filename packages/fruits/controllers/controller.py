from abc import ABC, abstractmethod

from fruits.game_entity import GameEntity


class Controller(ABC):

    def __init__(self, entity: GameEntity):
        self.entity = entity

    @property
    @abstractmethod
    def listening_events(self) -> list: ...

    @abstractmethod
    def receive(self, command) -> None: ...

