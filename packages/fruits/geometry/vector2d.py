import math
from typing import Union
import fruits.geometry.angle as angle2d


class Vector2D:

    def __init__(self, x: float = None, y: float = None) -> None:
        if x is None or y is None:
            self._invalid = True
            self.reset()
        else:
            self._invalid = False
            self._x = x
            self._y = y
            self._r = 0
            self._ang = 0
            self._update_polar()

    def _update_polar(self) -> None:
        if self._invalid:
            return
        self._r = math.hypot(self._x, self._y)
        self._ang = angle2d.fit(math.atan2(self._y, self._x), angle2d.MODE_ZERO_2PI)

    def _update_cartesian(self) -> None:
        if self._invalid:
            return
        self.x = self._r * math.cos(self._ang)
        self.y = self._r * math.sin(self._ang)

    def reset(self) -> None:
        self._x = 0
        self._y = 0
        self._r = 0
        self._ang = 0

    @classmethod
    def from_polar(cls, r: float, ang: float) -> ' ':
        vec = Vector2D(0, 0)
        vec.r = r
        print("before", vec.ang, "expected", ang)
        vec.ang = ang
        print("result", vec.ang)
        return vec

    @property
    def invalid(self) -> bool:
        return self._invalid

    @invalid.setter
    def invalid(self, new_invalid) -> None:
        if new_invalid is True:
            # If invalid, reset vector ?
            # Another option would be to maintain last state. Something equivalent to "freezing" the vector
            self.reset()
        self._invalid = new_invalid

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, new_x: float) -> None:
        if new_x is None:
            self._invalid = True
        else:
            self._invalid = False
            self._x = new_x
            self._update_polar()

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, new_y: float) -> None:
        if new_y is None:
            self._invalid = True
        else:
            self._invalid = False
            self._y = new_y
            self._update_polar()

    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, new_r: float) -> None:
        if new_r is None:
            self._invalid = True
        else:
            self._invalid = False
            if new_r < 0:
                new_r = 0
            self._r = new_r
            self._update_cartesian()

    @property
    def ang(self) -> float:
        return self._ang

    @ang.setter
    def ang(self, new_ang: float) -> None:
        if new_ang is None:
            self._invalid = True
        else:
            new_ang = angle2d.fit(new_ang, angle2d.MODE_ZERO_2PI)

            self._invalid = False
            self._ang = new_ang
            self._update_cartesian()

    def __add__(self, other) -> 'Vector2D':
        if isinstance(other, Vector2D):
            if self._invalid or other.invalid:
                return Vector2D()
            return Vector2D(self._x + other.x, self._y + other.y)
        raise TypeError

    __radd__ = __add__

    def __sub__(self, other) -> 'Vector2D':
        if isinstance(other, Vector2D):
            if self._invalid or other.invalid:
                return Vector2D()
            return Vector2D(self._x - other.x, self._y - other.y)
        raise TypeError

    def __mul__(self, other) -> Union['Vector2D', float]:
        if self._invalid:
            return Vector2D()

        if isinstance(other, Vector2D):
            if other.invalid:
                return Vector2D()
            else:
                return self._x * other.x + self._y * other.y
        elif isinstance(other, float) or isinstance(other, int):
            return Vector2D(self._x * other, self._y * other)

        raise TypeError

    __rmul__ = __mul__
