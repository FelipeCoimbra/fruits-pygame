from abc import ABC, abstractmethod
import fruits.command


class Scene(ABC):

    def __init__(self) -> None:
        self._enable_user_commands = True
        self._world_state = None
        self._game_objects = {}

    def enable_user_commands(self, enable) -> None:
        self._enable_user_commands = enable

    @abstractmethod
    def init(self) -> None:
        pass

    @abstractmethod
    def update(self, user_commands) -> None:
        pass

    def apply_physics(self, engine):
        pass


class MainScene(Scene):

    def __init__(self) -> None:
        super(MainScene, self).__init__()

    def init(self) -> None:
        pass

    def update(self, user_commands) -> None:
        if self._enable_user_commands:
            if user_commands.get(fruits.command.Command.UP) is not None:
                c = user_commands.get(fruits.command.Command.UP).get_count()
                print("PRESSED UP " + str(c) + "times")
            if user_commands.get(fruits.command.Command.DOWN) is not None:
                print("PRESSED DOWN")
            if user_commands.get(fruits.command.Command.LEFT) is not None:
                print("PRESSED LEFT")
            if user_commands.get(fruits.command.Command.RIGHT) is not None:
                print("PRESSED RIGHT")
            if user_commands.get(fruits.command.Command.SPACE) is not None:
                print("PRESSED SPACE")
            if user_commands.get(fruits.command.Command.ESCAPE) is not None:
                print("PRESSED ESC")

