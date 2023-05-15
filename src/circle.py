from src.figure import Figure


class Circle(Figure):
    def __init__(self, a: int):
        super().__init__()
        self.a = a
        self.name = 'Circle'
        Circle.error(self)

    @property
    def circle_area(self):
        pi = 3.14
        return pi * (self.a ** 2)

    @property
    def circle_perimeter(self):
        pi = 3.14
        return (pi * self.a) * 2

    def error(self):
        if self.a <= 0:
            raise ValueError('ValueError')
