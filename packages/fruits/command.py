

class Command:

    # User Actions
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    SPACE = 4
    ESCAPE = 5

    def __init__(self, action) -> None:
        self.__frame_count = 1
        self.__action = action

    def increment_count(self) -> None:
        self.__frame_count = self.__frame_count + 1

    def get_action(self) -> int:
        return self.__action

    def get_count(self) -> int:
        return self.__frame_count


