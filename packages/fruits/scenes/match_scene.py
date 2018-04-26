from fruits.background import Background
from fruits.match import Match
from fruits.scenes.scene import Scene
from fruits.world import FruitsWorld
from fruits.scenes.menu_scene import MenuScene


class MatchScene(Scene):
    def __init__(self, event_handler) -> None:
        super(MatchScene, self).__init__(event_handler,
                                         FruitsWorld(),
                                         Background('blue-background.png'))
        self.__match = Match(self)
        self._event_handler.subscribe_entity(self.__match)
        for entity in self._world.drawables:
            self._event_handler.subscribe_entity(entity)

    def play(self) -> None:
        Scene.play(self)

    def stop(self) -> None:
        Scene.stop(self)

    def pause(self) -> None:
        Scene.pause(self)

    def _user_update(self, user_commands) -> None:
        if self.status() == Scene.ALIVE and self.user_commands_enabled():
            self._event_handler.process_events(user_commands)

    def _apply_physics(self, engine) -> None:
        if self.status() == Scene.ALIVE:
            engine.move_fruits()

    def _update_final_state(self) -> None:
        if self.status() == Scene.DONE or self.status() == Scene.PAUSED:
            # Scene has received signal to terminate/pause
            # Just enqueue next scene and return
            self._enqueue_next_scene()
            return
        # Update Match according to new world
        # TODO

    def _enqueue_next_scene(self):
        # TODO: Differentiate next scene of QUIT from next scene of end of match
        if self.status() == Scene.PAUSED:
            self._enqueued_scene = MenuScene(self._event_handler)
        else:
            self._enqueued_scene = None

    def draw_background(self, screen) -> None:
        if self._background is not None and self._background.mesh.image is not None:
            self._background.mesh.draw_on(screen)

    def draw_world(self, screen) -> None:
        if self._world is not None:
            drawables = self._world.drawables
            for drawable in drawables:
                if drawable.mesh.image is not None:
                    drawable.mesh.draw_on(screen)

            # if self._world.current_player != -1:
            #     labels = [
            #         {
            #             'label': pygame.font.SysFont("bitstreamverasans", 20, bold=(self._world.current_player == 0)
            #                                          ).render("PLAYER 1", 1, (255, 0, 0)),
            #             'pos': (10, 10)
            #         },
            #         {
            #             'label': pygame.font.SysFont("bitstreamverasans", 20, bold=(self._world.current_player == 1)
            #                                          ).render("PLAYER 2", 1, (0, 128, 0)),
            #             'pos': (shared.window_width - 105, 10)
            #         }
            #     ]
            #
            #     for label in labels:
            #         screen.blit(label['label'], label['pos'])
            #     pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 35, 95, 20))
            #     pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(shared.window_width - 105, 35, 95, 20))
