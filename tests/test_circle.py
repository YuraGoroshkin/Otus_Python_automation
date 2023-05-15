from random import randrange
from src.circle import Circle


def test_сircle():
    a = randrange(100)
    сircle = Circle(a)
    assert сircle.circle_area == area(a)
    assert сircle.name == 'Circle'


def area(a):
    pi = 3.14
    s = pi * (a ** 2)
    return s
