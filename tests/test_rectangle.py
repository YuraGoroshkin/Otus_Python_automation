from src.rectangle import Rectangle
from random import randrange


def test_rectangle():
    a = randrange(10)
    b = randrange(10)
    rectangle = Rectangle(a, b)
    rectangle.rectangle_area()
    assert rectangle.area == area(a, b)
    assert rectangle.name == 'Rectangle'


def area(a, b):
    s = a * b
    return s
