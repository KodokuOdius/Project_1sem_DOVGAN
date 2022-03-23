_a = 7
_b = 2
_c = 8


def triangle_perimeter(a=_a, b=_b, c=_c):
    return a + b + c


def triangle_area(a=_a, b=_b, c=_c):
    p = triangle_perimeter(a, b, c) / 2

    return (p * (p - a) * (p - b) * (p - c)) ** .5