from src.figure import Figure


class Circle(Figure):
    def __init__(self, a: int):
        super().__init__()
        self.a = a
        self.name = 'Circle'
        Circle.error(self)

    def circle_area(self):
        pi = 3.14
        self.area = pi * (self.a ** 2)
        return self.area

    def circle_perimeter(self):
        pi = 3.14
        self.perimeter = (pi * self.a) * 2
        return self.perimeter

    def error(self):
        if self.a <= 0:
            raise ValueError('ValueError')
