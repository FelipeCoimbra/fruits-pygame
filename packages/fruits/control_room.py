import fruits.scene

class SceneManager:

    def __init__(self) -> None:
        self.__scene = None
        self.__physics_engine = None
        self.__init_first_scene()

    def __init_first_scene(self) -> None:
        self.__scene = fruits.scene.MainScene()

    def manage(self, user_commands) -> None:
        if self.__scene is None:
            return

        self.__scene.update(user_commands)
        if self.__physics_engine is not None:
            self.__scene.apply_physics(self.__physics_engine)



