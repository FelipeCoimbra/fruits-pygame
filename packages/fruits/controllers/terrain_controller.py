from fruits.controllers.controller import Controller
from fruits.game_entity import GameEntity
from fruits.command import Command


class TerrainController(Controller):

    def __init__(self, terrain_entity: 'Terrain'):
        super().__init__(terrain_entity)
        self.events = [Command.RIGHT_MOUSE_START]

    @property
    def listening_events(self):
        return self.events

    def receive(self, command: str) -> None:
        if not self.entity.is_selected:
            return
        if command == Command.RIGHT_MOUSE_START:
            print("oi")
            self.entity.destroy()
