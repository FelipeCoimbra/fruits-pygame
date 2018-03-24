from fruits.scenes.scene import Scene
from fruits.scenes.match_scene import MatchScene
from fruits.game_event import EventHandler


class SceneManager:

    def __init__(self) -> None:
        self.__current_scene = None
        self.__scene_stack = []
        self.__physics_engine = None
        self.__event_handler = EventHandler()
        self.__change_scene(MatchScene(self.__event_handler))

    def __change_scene(self, scene) -> bool:
        # Change to the desired scene if valid. Else search for last valid scene
        if self.__current_scene is not None and self.__current_scene.status() == Scene.PAUSED:
            self.__scene_stack.append(self.__current_scene)

        while scene is None and len(self.__scene_stack) > 0:
            scene = self.__scene_stack.pop()

        if scene is None:
            self.__handle_exit()
            return False
        else:
            self.__current_scene = scene
            self.__current_scene.play()

        return True

    def manage(self, user_commands) -> bool:
        if self.__current_scene is None:
            return False

        self.__current_scene.update(user_commands, self.__physics_engine)

        if self.__current_scene.status() == Scene.DONE:
            new_scene = self.__current_scene.next_scene()
            return self.__change_scene(new_scene)

        return True

    def draw_scene(self, screen) -> None:
        # Draw scene drawable content into a given screen
        if self.__current_scene is None:
            return
        self.__current_scene.draw_background(screen)
        self.__current_scene.draw_world(screen)

    def __handle_exit(self) -> None:
        # Do any remaining tasks before exiting
        pass
