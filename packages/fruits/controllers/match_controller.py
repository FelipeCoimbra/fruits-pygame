from fruits.controllers.controller import Controller
from fruits.command import Command
from fruits.events.explosion import ExplosionEvent, ToggleTeamEvent
from fruits.explosion_effect import ExplosionEffectEvent


class MatchController(Controller):
    listening_events = [
        Command.QUIT, Command.TAB, Command.X_KEY,
        Command.MOUSE_LEFT_DOWN, ExplosionEvent,
        Command.ESCAPE, ExplosionEffectEvent,
        Command.Q, Command.W, Command.C
    ]

    def __init__(self, match_entity: 'Match'):
        super(MatchController, self).__init__(match_entity)
        self.equipped = False

    def receive(self, command):
        if command == Command.QUIT:
            self.entity.interrupt()
        elif command == Command.TAB:
            self.entity.update_current_fruit()
        elif command == Command.X_KEY:
            if not self.equipped:
                self.equipped = True
                self.entity.equip_bomb()
        elif command == Command.C:
            if self.equipped:
                self.entity.desequip_bomb()
                self.equipped = False
        elif command == Command.MOUSE_LEFT_DOWN:
            if self.equipped:
                # self.entity.disable_user_input()
                self.equipped = False
        elif isinstance(command, ExplosionEvent):
            self.entity.bomb_exploded(command.bomb)
        elif isinstance(command, ExplosionEffectEvent):
            self.entity.fade_explosion_effect(command.explosion_effect)
        elif isinstance(command, ToggleTeamEvent):
            self.entity.update_current_player()
        # elif command == Command.W:
        #     self.entity._Match__scene.pause()
