from random import randrange
from src.circle import Circle
import pytest


def test_сircle_area():
    a = randrange(100)
    сircle = Circle(a)
    assert сircle.circle_area == area(a)
    assert сircle.name == 'Circle'


def test_сircle_perimetr():
    a = randrange(100)
    сircle = Circle(a)
    сircle.circle_perimeter()
    assert сircle.perimeter == perimetr(a)
    assert сircle.name == 'Circle'


def test_create_circle_negative():
    with pytest.raises(ValueError):
        Circle(-1)


def test_create_circle_zero():
    with pytest.raises(ValueError):
        Circle(0)


def area(a):
    pi = 3.14
    s = pi * (a ** 2)
    return s


def perimetr(a):
    pi = 3.14
    return (pi * a) * 2
