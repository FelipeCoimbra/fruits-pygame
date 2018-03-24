from abc import ABC, abstractmethod
import fruits.command
import fruits.world
import fruits.shared_preferences as shared
import fruits.game_event


class Scene(ABC):
    def __init__(self) -> None:
        self._enable_user_commands = True
        self._done = False
        self._world = None
        self._event_handler = None

    def enable_user_commands(self, enable) -> None:
        self._enable_user_commands = enable

    @abstractmethod
    def init(self) -> None:
        pass

    def update(self, user_commands, engine=None) -> None:
        self._user_update(user_commands)
        if engine is not None:
            self._apply_physics(engine)
        self._update_final_state()

    def done(self) -> bool:
        return self._done

    @abstractmethod
    def _user_update(self, user_commands) -> None:
        pass

    def _apply_physics(self, engine) -> None:
        pass

    @abstractmethod
    def _update_final_state(self) -> None:
        pass

    def exit_scene(self) -> '':
        pass


class MainScene(Scene):
    def __init__(self) -> None:
        super(MainScene, self).__init__()
        self.__background = fruits.background.Background('blue-background.png',
                                                         (shared.window_width, shared.window_height))
        self._world = fruits.world.FruitsWorld()
        self._event_handler = fruits.game_event.EventHandler()

    def init(self) -> None:
        pass

    def _user_update(self, user_commands) -> None:
        self._event_handler.notify_commands()

        if self._enable_user_commands:
            if user_commands.get(fruits.command.Command.UP) is not None:
                c = user_commands.get(fruits.command.Command.UP).count
                print("PRESSED UP", c, "times")
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

    def _apply_physics(self, engine) -> None:
        pass

    def _update_final_state(self) -> None:
        pass
