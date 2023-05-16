from src.rectangle import Rectangle
from random import randrange
import pytest


def test_rectangle_area():
    a = randrange(10)
    b = randrange(10)
    rectangle = Rectangle(a, b)
    assert rectangle.area == area(a, b)
    assert rectangle.name == 'Rectangle'


def test_rectangle_perimetr():
    a = randrange(10)
    b = randrange(10)
    rectangle = Rectangle(a, b)
    rectangle.perimeter
    assert rectangle.perimeter == perimetr(a, b)
    assert rectangle.name == 'Rectangle'


def test_create_rectangle_negative():
    with pytest.raises(ValueError):
        Rectangle(-1, 2)


def test_create_rectangle_zero():
    with pytest.raises(ValueError):
        Rectangle(0, 2)


def test_create_rectangle_equal_sides():
    with pytest.raises(ValueError):
        Rectangle(2, 2)


def area(a, b):
    s = a * b
    return s


def perimetr(a, b):
    return (a + b) * 2
