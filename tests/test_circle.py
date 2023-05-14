from random import randrange
from src.circle import Circle


def test_сircle():
    a = randrange(100)
    сircle = Circle(a)
    сircle.circle_area()
    result = Circle.area
    assert result == area(a)


def area(a):
    pi = 3.14
    s = pi * (a ** 2)
    return s
