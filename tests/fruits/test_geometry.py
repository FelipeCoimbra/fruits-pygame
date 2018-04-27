import fruits.geometry.vector2d as vec2d
import math


def eq(a: float, b: float) -> bool:
    eps = 0.000001
    return math.fabs(a - b) < eps


A = vec2d.Vector2D()
assert A.invalid

A.invalid = False

A.reset()
assert eq(A.x, 0) and eq(A.y, 0) and eq(A.r, 0) and eq(A.ang, 0)

A.x = math.sqrt(3)/2
A.y = 0.5
assert eq(A.ang, math.pi/6) and eq(A.r, 1)

B = vec2d.Vector2D(0, 1)

assert eq((A+B).x, math.sqrt(3)/2) and eq((A+B).y, 1.5)
assert eq((A+B).x, (B+A).x) and eq((A+B).y, (B+A).y)

assert eq((A-B).r, 1) and eq((A-B).ang, 11*math.pi/6)
assert eq((A-B).r, (B-A).r) and eq((A-B).ang, (B-A).ang + math.pi)

assert eq((2*A).x, math.sqrt(3)) and eq((2*A).y, 1)
assert eq((2*A).x, (A*2).x) and eq((2*A).y, (A*2).y)
assert eq((2*A).x, (A*2).x) and eq((2*A).y, (A*2).y)

