from src.figure import Figure


class Triangle(Figure):

    def __init__(self, a: int, b: int, c: int):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def triangle_area(self):
        Triangle.error(self)
        p = Triangle.triangle_perimeter(self) / 2  # расчет полупериметра для формулы Герона
        Triangle.area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5  # расчет площади по формуле Герона
        return Triangle.area

    def triangle_perimeter(self):
        Triangle.error(self)
        Triangle.perimeter = self.a + self.b + self.c
        return Triangle.perimeter

    @staticmethod
    def add_area(value):
        return Triangle.area + value

    def error(self):
        if self.a <= 0:
            raise ValueError('ValueError')
        if self.b <= 0:
            raise ValueError('ValueError')
        if self.c <= 0:
            raise ValueError('ValueError')
        if self.a + self.b < self.c:
            raise ValueError('ValueError')
        if self.a + self.c < self.b:
            raise ValueError('ValueError')
        if self.b + self.c < self.a:
            raise ValueError('ValueError')
