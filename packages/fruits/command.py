

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

    def increment_count(self):
        self.count = self.count + 1

    @property
    def count(self):
        return self.__frame_count

    @count.setter
    def count(self, value):
        self.__frame_count = value