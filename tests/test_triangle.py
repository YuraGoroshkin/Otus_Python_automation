from src.triangle import Triangle
from random import randrange
import pytest


def test_triangle_area():
    a = randrange(10)
    b = randrange(10)
    c = randrange(10)
    triangle = Triangle(a, b, c)
    triangle.triangle_area()
    assert triangle.area == area(a, b, c)
    assert triangle.name == 'Triangle'


def test_triangle_perimetr():
    a = randrange(10)
    b = randrange(10)
    c = randrange(10)
    triangle = Triangle(a, b, c)
    triangle.triangle_perimeter()
    assert triangle.perimeter == perimetr(a, b, c)
    assert triangle.name == 'Triangle'


def test_create_triangle_negative():
    with pytest.raises(ValueError):
        Triangle(-1, 3, 3)
    with pytest.raises(ValueError):
        Triangle(-1, -1, 3)
    with pytest.raises(ValueError):
        Triangle(-1, -1, -1)


def test_create_triangle_zero():
    with pytest.raises(ValueError):
        Triangle(3, 0, 3)


def test_create_triangle_sum():
    with pytest.raises(ValueError):
        Triangle(1, 2, 9)


def area(a, b, c):
    p = (a + b + c) / 2  # расчет полупериметра для формулы Герона
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5  # расчет площади по формуле Герона
    return s


def perimetr(a, b, c):
    return a + b + c
