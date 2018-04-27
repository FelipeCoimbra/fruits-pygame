class ExplosionEvent:
    def __init__(self, position: tuple, bomb) -> None:
        self.position = position
        self.bomb = bomb

    def __str__(self) -> str:
        return f'{self.__class__.__name__} at {self.position}'


class ToggleTeamEvent:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'
