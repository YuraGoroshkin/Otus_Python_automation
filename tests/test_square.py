from src.square import Square
from random import randrange


def test_square():
    a = randrange(100)
    square = Square(a)
    square.square_area()
    assert area(a) == Square.area


def area(a):
    s = a * 2
    return s
