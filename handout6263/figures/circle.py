from math import pi as _pi


_default_radius = 5


def circle_perimeter(radius=_default_radius):
    return 2 * _pi * radius


def circle_area(radius=_default_radius):
    return _pi * radius * radius