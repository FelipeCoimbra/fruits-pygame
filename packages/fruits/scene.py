from abc import ABC, abstractmethod
import fruits.command
import fruits.background
import fruits.world
import fruits.terrain
import fruits.shared_preferences as shared
import fruits.game_event


class Scene(ABC):
    def __init__(self, world, background=None) -> None:
        self._enable_user_commands = True
        self._done = False
        self._event_handler = fruits.game_event.EventHandler()
        self._background = background
        self._world = world

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

    def draw_background(self, screen) -> None:
        pass

    def draw_world(self, screen) -> None:
        pass


class MainScene(Scene):
    def __init__(self) -> None:
        super(MainScene, self).__init__(fruits.world.FruitsWorld(),
                                        fruits.background.Background('blue-background.png'))

    def init(self) -> None:
        pass

    def _user_update(self, user_commands) -> None:
        if self._enable_user_commands:
        self._event_handler.process_events(user_commands)

    def _apply_physics(self, engine) -> None:
        pass

    def _update_final_state(self) -> None:
        pass

    def draw_background(self, screen) -> None:
        if self._background is not None and self._background.mesh is not None:
            self._background.mesh.draw_on(screen)

    def draw_world(self, screen) -> None:
        if self._world is not None:
            drawables = self._world.get_drawables()
            for drawable in drawables:
                if drawable.mesh is not None:
                    drawable.mesh.draw_on(screen)
