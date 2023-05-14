from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b

    def rectangle_area(self):
        Rectangle.error(self)
        Rectangle.area = self.a * self.b
        return Rectangle.area

    def rectangle_perimeter(self):
        Rectangle.error(self)
        Rectangle.perimeter = (self.a + self.b) * 2
        return Rectangle.perimeter

    @staticmethod
    def add_area(value):
        return Rectangle.area + value

    def error(self):
        if self.a <= 0:
            raise ValueError('ValueError')
        if self.b <= 0:
            raise ValueError('ValueError')
        if self.a == self.b:
            raise ValueError('ValueError')
