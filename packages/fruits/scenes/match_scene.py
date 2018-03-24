from fruits.background import Background
from fruits.match import Match
from fruits.scenes.scene import Scene
from fruits.world import FruitsWorld


class MatchScene(Scene):
    def __init__(self, event_handler) -> None:
        super(MatchScene, self).__init__(event_handler,
                                         FruitsWorld(),
                                         Background('blue-background.png'))
        self.__match = Match(self)
        self._event_handler.subscribe_entity(self.__match)

    def play(self) -> None:
        Scene.play(self)

    def stop(self) -> None:
        Scene.stop(self)

    def _user_update(self, user_commands) -> None:
        # Updates world with User Input Commands
        if self.status() == Scene.ALIVE and self.user_commands_enabled():
            self._event_handler.process_events(user_commands)

    def _apply_physics(self, engine) -> None:
        # Updates world with constraints of a physics engine
        if self.status() == Scene.ALIVE:
            pass

    def _update_final_state(self) -> None:
        # Update match general state after User and Physics updates
        if self.status() == Scene.DONE:
            # Scene has received signal to terminate
            # Just enqueue next scene and return
            self._enqueue_next_scene()
            return
        # Update Match according to new world
        # TODO

    def _enqueue_next_scene(self):
        # Enqueue next scene depending on current world state
        # TODO: Differentiate next scene of QUIT from next scene of end of match
        self._enqueued_scene = None

    def draw_background(self, screen) -> None:
        # Draws the Scene background in a given screen
        if self._background is not None and self._background.mesh is not None:
            self._background.mesh.draw_on(screen)

    def draw_world(self, screen) -> None:
        # Draws each of world game_objects' meshes in a given screen
        if self._world is not None:
            drawables = self._world.get_drawables()
            for drawable in drawables:
                if drawable.mesh is not None:
                    drawable.mesh.draw_on(screen)
