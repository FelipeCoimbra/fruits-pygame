from fruits.game_entity import GameEntity
from fruits.controllers.match_controller import MatchController


class Match(GameEntity):

    # Match status

    def __init__(self, scene) -> None:
        super(Match, self).__init__()
        self.__teams: list = []
        self.__scene = scene
        self.attach_controller(MatchController(self))

    def __set_conf(self, conf):
        self.__conf = conf.team_count

    def interrupt(self):
        # Ends match suddenly
        self.__scene.stop()

    def update_current_fruit(self):
        self.__scene._world.update_current_fruit()

    def disable_user_input(self) -> None:
        self.__scene.enable_user_commands(False)
        self.__scene.waiting_launching = False

    def equip_bomb(self) -> None:
        self.disable_user_input()
        self.__scene.equip_bomb()
        self.__scene.waiting_launching = True

    def desequip_bomb(self) -> None:
        self.__scene.desequip_bomb()
        self.__scene.enable_user_commands(True)
        self.__scene.waiting_launching = False

    def bomb_exploded(self, bomb) -> None:
        self.__scene.enable_user_commands(True)
        self.__scene.waiting_launching = False
        self.__scene.bomb_exploded(bomb)

    def fade_explosion_effect(self, explosion_effect) -> None:
        self.__scene.remove_effect(explosion_effect)

    def update_current_player(self):
        self.__scene._world.update_current_player()
