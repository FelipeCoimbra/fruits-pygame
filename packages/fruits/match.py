from fruits.game_entity import GameEntity
from fruits.controllers.match_controller import MatchController


class Match(GameEntity):

    # Match status

    def __init__(self, scene) -> None:
        super(Match, self).__init__()
        self.__teams: list = []
        self.__scene = scene
        self.__bomb = None
        self.__explosion_eff = None
        self.__holding_fruit = None

        self.attach_controller(MatchController(self))

    @property
    def bomb(self):
        return self.__bomb

    @bomb.setter
    def bomb(self, bomb):
        self.__bomb = bomb

    @property
    def explosion_eff(self):
        return self.__explosion_eff

    @explosion_eff.setter
    def explosion_eff(self, eff):
        self.__explosion_eff = eff

    @property
    def holding_fruit(self):
        return self.__holding_fruit

    @holding_fruit.setter
    def holding_fruit(self, fruit):
        self.__holding_fruit = fruit

    def interrupt(self):
        # Ends match suddenly
        self.__scene.stop()

    def update_current_fruit(self):
        self.__scene._world.update_current_fruit()

    def disable_user_input(self) -> None:
        self.__scene.enable_user_commands(False)

    def enable_user_input(self) -> None:
        self.__scene.enable_user_commands(True)

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
