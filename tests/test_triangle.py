from src.triangle import Triangle


def test_triangle():
    triangle = Triangle(a=10, b=10, c=10)
    print(triangle.triangle_area())
