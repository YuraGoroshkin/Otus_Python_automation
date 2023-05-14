from src.figure import Figure


class Circle(Figure):
    def __init__(self, a: int):
        super().__init__()
        self.a = a

    def circle_area(self):
        Circle.error(self)
        pi = 3.14
        Circle.area = pi * (self.a ** 2)
        return Circle.area

    def circle_perimeter(self):
        Circle.error(self)
        pi = 3.14
        Circle.perimeter = (pi * self.a) * 2
        return Circle.perimeter

    @staticmethod
    def add_area(value):
        return Circle.area + value

    def error(self):
        if self.a <= 0:
            raise ValueError('ValueError')
