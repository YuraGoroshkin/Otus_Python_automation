from src.triangle import Triangle
from random import randrange


def test_triangle():
    a = randrange(10)
    b = randrange(10)
    c = randrange(10)
    triangle = Triangle(a, b, c)
    triangle.triangle_area()
    assert triangle.area == area(a, b, c)
    assert triangle.name == 'Triangle'


def area(a, b, c):
    p = (a + b + c) / 2  # расчет полупериметра для формулы Герона
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5  # расчет площади по формуле Герона
    return s
