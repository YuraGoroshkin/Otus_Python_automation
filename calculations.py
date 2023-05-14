from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle

# triangle = Triangle(2, 5, 4)
# triangle.triangle_area()
# c = Triangle.area
# print(c)

# rectangle = Rectangle(10, 1)
# rectangle.rectangle_area()
# b = Rectangle.area
# print(b)
#
square = Square(1)
square.square_area()
c = square.area
print("Первое  " + str(c))
# #
сircle = Circle(1)
сircle.circle_area()
d = Circle.area
c = сircle.circle_area()
f = сircle.area
print("два  " + str(c))
print("три  " + str(d))
print("четыре  " + str(f))
# #
# print(triangle.add_area(Rectangle.area))
# print(rectangle.add_area(Triangle.area))
# print(rectangle.add_area(Rectangle.area))
# print(rectangle.add_area(Square.area))
print(сircle.add_area(square))
print(square.add_area(сircle))
