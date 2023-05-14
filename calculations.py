from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle


triangle = Triangle(13, 10, 10)
triangle.triangle_area()
c = Triangle.area
print(c)

rectangle = Rectangle(5, 4)
rectangle.rectangle_area()
b = Rectangle.area
print(b)

square = Square(7)
square.square_area()
c = Square.area
print(c)

сircle = Circle(2)
сircle.circle_area()
d = Circle.area
print(d)

print(triangle.add_area(Rectangle.area))
print(rectangle.add_area(Triangle.area))
print(rectangle.add_area(Rectangle.area))
print(rectangle.add_area(Square.area))
print(square.add_area(Circle.area))