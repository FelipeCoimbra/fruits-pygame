import fruits.scene


class SceneManager:

    def __init__(self) -> None:
        self.__scene = None
        self.__physics_engine = None
        self.__change_scene(fruits.scene.MainScene())

    def __change_scene(self, scene) -> None:
        if scene is None:
            self.__scene = fruits.scene.MainScene()
        else:
            self.__scene = scene
        self.__scene.init()

    def manage(self, user_commands) -> None:
        if self.__scene is None:
            return

        self.__scene.update(user_commands, self.__physics_engine)

        if self.__scene.done():
            new_scene = self.__scene.exit()
            self.__change_scene(new_scene)


