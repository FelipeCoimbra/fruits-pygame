

class Command:

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    SPACE = 4
    ESCAPE = 5

    def __init__(self, action):
        self.count = 0
        self.action = action

    def increment_count(self):
        self.count = self.count + 1
