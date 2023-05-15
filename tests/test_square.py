from src.square import Square
from random import randrange


def test_square():
    a = randrange(100)
    square = Square(a)
    assert area(a) == square.square_area
    assert square.name == 'Square'


def area(a):
    s = a * 2
    return s
