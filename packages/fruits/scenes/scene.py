from abc import ABC, abstractmethod
from fruits.world import World
from fruits.game_event import EventHandler


class Scene(ABC):

    # Scene status
    ALIVE = 0
    PAUSED = 1
    DONE = 2

    def __init__(self, event_handler: EventHandler, world: World, background=None) -> None:
        self.__user_commands_enable = True
        self.__status = Scene.ALIVE
        self._enqueued_scene = None
        self._event_handler = event_handler
        self._background = background
        self._world = world

    def user_commands_enabled(self) -> bool:
        return self.__user_commands_enable

    def enable_user_commands(self, enable) -> None:
        self.__user_commands_enable = enable

    @abstractmethod
    def play(self) -> None:
        # Initializes internal structure and plays scene
        if self.status() == Scene.PAUSED:
            self._set_status(Scene.ALIVE)

    @abstractmethod
    def stop(self) -> None:
        # Stops scene
        self._set_status(Scene.DONE)

    def update(self, user_commands, engine=None) -> None:
        # Updates Scene state
        if self.status() == Scene.ALIVE:
            self._user_update(user_commands)
            if engine is not None:
                self._apply_physics(engine)
        self._update_final_state()

    def status(self) -> int:
        return self.__status

    def _set_status(self, status) -> None:
        self.__status = status

    @abstractmethod
    def _user_update(self, user_commands) -> None:
        # Updates world with User Input Commands
        pass

    def _apply_physics(self, engine) -> None:
        # Updates world with constraints of a physics engine
        pass

    @abstractmethod
    def _update_final_state(self) -> None:
        # Update match general state after User and Physics updates
        pass

    @abstractmethod
    def _enqueue_next_scene(self) -> None:
        # Enqueue next scene depending on current world state
        pass

    def next_scene(self) -> '':
        return self._enqueued_scene

    def draw_background(self, screen) -> None:
        # Draws the Scene background in a given screen
        pass

    def draw_world(self, screen) -> None:
        # Draws each of world game_objects' meshes in a given screen
        pass


