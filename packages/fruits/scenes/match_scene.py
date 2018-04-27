from fruits.background import Background
from fruits.match import Match
from fruits.scenes.scene import Scene
from fruits.world import FruitsWorld
from fruits.bomb import Bomb
from fruits.fruit import Fruit
from fruits.events.explosion import ExplosionEvent
from fruits.command import Command
from fruits.explosion_effect import ExplosionEffect
from fruits.geometry.vector2d import Vector2D
import pygame
import fruits.shared_preferences as shared
from functools import reduce


class MatchScene(Scene):
    def __init__(self, event_handler) -> None:
        super(MatchScene, self).__init__(event_handler,
                                         FruitsWorld(),
                                         Background('blue-background.png'))
        self.__match = Match(self)
        self.waiting_launching = False
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
        if self.status() != Scene.ALIVE:
            return

        self._event_handler.process_events(user_commands)
        if self.waiting_launching:
            commands = [c for c in user_commands
                        if (isinstance(c, ExplosionEvent)
                            or c in (Command.MOUSE_LEFT_DOWN, Command.ESCAPE))]
            self._event_handler.process_events(commands)


    def _apply_physics(self, engine) -> None:
        if self.status() == Scene.ALIVE:
            if self.user_commands_enabled():
                engine.apply_user_commands()
            else:
                engine.negate()
            engine.apply_fields()
            if self.__match.bomb is not None:
                self.__match.bomb.update_frame()
            engine.apply_destruction()

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
            
            if self._world.current_player != -1:
                labels = [
                    {
                        'label': pygame.font.SysFont("bitstreamverasans", 20, bold=(self._world.current_player == 0)
                                                     ).render("PLAYER 1", 1, (255, 0, 0)),
                        'pos': (10, 10)
                    },
                    {
                        'label': pygame.font.SysFont("bitstreamverasans", 20, bold=(self._world.current_player == 1)
                                                     ).render("PLAYER 2", 1, (0, 128, 0)),
                        'pos': (shared.window_width - 105, 10)
                    }
                ]

                for label in labels:
                    screen.blit(label['label'], label['pos'])

                player_0_fruits = list(filter(lambda f: not f.player, self._world.fruits))
                total_player_0_stamina = reduce(lambda acc, x: acc + x.stamina, player_0_fruits, 0.0)
                player_0_width = 95 * total_player_0_stamina / 500

                player_1_fruits = list(filter(lambda f: f.player, self._world.fruits))
                total_player_1_stamina = reduce(lambda acc, x: acc + x.stamina, player_1_fruits, 0.0)
                player_1_width = 95 * total_player_1_stamina / 500

                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 35, player_0_width, 20))
                pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(shared.window_width - 105, 35, player_1_width, 20))

    def equip_bomb(self) -> None:
        current_fruit: Fruit = self._world.fruits[self._world.current_fruit]
        current_fruit.toggle_block_movement()
        fruit_x, fruit_y = current_fruit.position.x, current_fruit.position.y
        print(f'Creating bomb at: {fruit_x}, {fruit_y - 5}')
        bomb = Bomb(Vector2D(fruit_x, fruit_y - 5))
        self._world.bomb = bomb
        self._world.register(bomb)
        self._event_handler.subscribe_entity(bomb)
        self.__match.bomb = bomb
        self.__match.holding_fruit = current_fruit

    def desequip_bomb(self) -> None:
        try:
            self._world._drawables.remove(self.__match.bomb)
        except ValueError:
            print('Bomb desequiped and not in world!')
            print(f'Bomb element: ')
            print(f'World drawables: {self._world.drawables}')
        self._event_handler.unsubscribe_entity(self.__match.bomb)
        self.__match.holding_fruit._blocked = False

    def bomb_exploded(self, bomb) -> None:
        try:
            self._world._drawables.remove(bomb)
            effect = ExplosionEffect(self.__match.bomb.position)
            self._world._drawables.append(effect)
            self._world.damage_fruits(bomb.position)
        except ValueError:
            print('Bomb exploded and not in world!')
            print(f'Bomb element: {bomb}')
            print(f'World drawables: {self._world._drawables}')

    def remove_effect(self, explosion_effect: ExplosionEffect) -> None:
        try:
            self._world._drawables.remove(explosion_effect)
        except ValueError:
            print('Explosion effect faded and not in world!')
            print(f'ExplosionEffect element:  {explosion_effect}')
            print(f'World drawables: {self._world._drawables}')
