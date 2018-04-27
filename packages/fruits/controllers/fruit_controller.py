from fruits.controllers.controller import Controller
from fruits.command import Command


class FruitController(Controller):

    def __init__(self, fruit_entity: 'Fruit'):
        super().__init__(fruit_entity)
        self.events = [Command.LEFT_START, Command.LEFT_END, Command.RIGHT_START, Command.RIGHT_END,
                       Command.SPACE_START]

    @property
    def listening_events(self):
        return self.events

    def receive(self, command: str) -> None:
        if not self.entity.is_selected:
            return
        if command == Command.LEFT_START:
            print("start walk")
            self.entity.walk(False)
        if command == Command.LEFT_END:
            print("end walk")
            self.entity.stop_walk(False)
        if command == Command.RIGHT_START:
            self.entity.walk(True)
        if command == Command.RIGHT_END:
            self.entity.stop_walk(True)
        if command == Command.SPACE_START:
            self.entity.jump()

