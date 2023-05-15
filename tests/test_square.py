from src.square import Square
from random import randrange
import pytest


def test_square_area():
    a = randrange(100)
    square = Square(a)
    square.square_area()
    assert square.area == area(a)
    assert square.name == 'Square'


def test_square_perimetr():
    a = randrange(100)
    square = Square(a)
    square.square_perimeter()
    assert square.perimeter == perimetr(a)
    assert square.name == 'Square'


def test_create_square_negative():
    with pytest.raises(ValueError):
        Square(-1)


def test_create_square_zero():
    with pytest.raises(ValueError):
        Square(0)


def area(a):
    s = a * 2
    return s


def perimetr(a):
    return a * 4
