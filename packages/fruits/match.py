from fruits.game_entity import GameEntity
from fruits.controllers.match_controller import MatchController
from random import randint
from fruits.fruit import Fruit


class Match(GameEntity):

    # Match status

    def __init__(self, scene):
        super(Match, self).__init__()
        self.__teams = []
        self.__scene = scene
        self.attach_controller(MatchController(self))

    def __set_conf(self, conf):
        self.__conf = conf.team_count

    def interrupt(self):
        # Ends match suddenly
        self.__scene.stop()

    def update_current_fruit(self):
        self.__scene._world.update_current_fruit()
