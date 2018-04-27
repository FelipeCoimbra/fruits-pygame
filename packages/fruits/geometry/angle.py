import math

MODE_ZERO_2PI = 0
MODE_MINUSPI_PI = 1


def fit(angle: float, mode: int) -> float:
    if angle > 2 * math.pi:
        angle -= math.floor(angle / (2 * math.pi)) * 2 * math.pi
    elif angle < 0:
        angle -= math.ceil(angle / (2 * math.pi)) * 2 * math.pi

    if mode == MODE_ZERO_2PI:
        return angle
    if mode == MODE_MINUSPI_PI and angle > math.pi:
        return angle - 2*math.pi
