from abc import ABC, abstractmethod


class Controller(ABC):
    @property
    @abstractmethod
    def listening_events(self) -> list: ...

    @abstractmethod
    def receive(self, event) -> None: ...

