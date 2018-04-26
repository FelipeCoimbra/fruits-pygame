from pygame import *


class Command:
    UP_START = 'UP_START'
    UP_END = 'UP_END'
    DOWN_START = 'DOWN_START'
    DOWN_END = 'DOWN_END'
    LEFT_START = 'LEFT_START'
    LEFT_END = 'LEFT_END'
    RIGHT_START = 'RIGHT_START'
    RIGHT_END = 'RIGHT_END'
    SPACE_START = 'SPACE_START'
    SPACE_END = 'SPACE_END'
    ESCAPE = 'ESCAPE'
    ENTER = 'ENTER'
    TAB = 'TAB'
    Q = 'Q'
    W = 'W'
    QUIT = 'QUIT'


commands = {
    (KEYDOWN, K_UP): Command.UP_START,
    (KEYUP, K_UP): Command.UP_END,
    (KEYDOWN, K_DOWN): Command.DOWN_START,
    (KEYUP, K_DOWN): Command.DOWN_END,
    (KEYDOWN, K_LEFT): Command.LEFT_START,
    (KEYUP, K_LEFT): Command.LEFT_END,
    (KEYDOWN, K_RIGHT): Command.RIGHT_START,
    (KEYUP, K_RIGHT): Command.RIGHT_END,
    (KEYDOWN, K_SPACE): Command.SPACE_START,
    (KEYUP, K_SPACE): Command.SPACE_END,
    (KEYDOWN, K_ESCAPE): Command.ESCAPE,
    (KEYDOWN, K_TAB): Command.TAB,
    (KEYDOWN, K_q): Command.Q,
    (KEYDOWN, K_w): Command.W,
    (KEYDOWN, K_g): Command.ENTER,
    QUIT: Command.QUIT
}
