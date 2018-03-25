from abc import ABC, abstractmethod
from typing import List, Tuple


class Controller(ABC):
    @property
    @abstractmethod
    def listening_events(self) -> List[Tuple[int, bool]]: ...

    @abstractmethod
    def receive(self, event) -> None: ...

