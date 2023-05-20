from random import randrange
from src.circle import Circle
from src.square import Square


def test_сircle_and_square():
    a = randrange(100)
    сircle = Circle(a)
    сircle.area
    square = Square(a)
    square.area
    assert сircle.add_area(square) == area_square(a) + area_circle(a)
    assert square.add_area(сircle) == area_square(a) + area_circle(a)


def area_circle(a):
    pi = 3.14
    s = pi * (a ** 2)
    return s


def area_square(a):
    s = a * 2
    return s

