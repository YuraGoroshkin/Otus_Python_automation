from src.figure import Figure


class Triangle(Figure):

    def __init__(self, a: int, b: int, c: int):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Triangle'
        Triangle.error(self)

    @property
    def triangle_area(self):
        p = self.triangle_perimeter / 2  # расчет полупериметра для формулы Герона
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5  # расчет площади по формуле Герона

    @property
    def triangle_perimeter(self):
        return self.a + self.b + self.c

    def error(self):
        if self.a <= 0:
            raise ValueError(f'Side a must be greater than 0, got {self.a}')
        if self.b <= 0:
            raise ValueError(f'Side a must be greater than 0, got {self.b}')
        if self.c <= 0:
            raise ValueError(f'Side a must be greater than 0, got {self.c}')
        if self.a + self.b < self.c:
            raise ValueError(f'Sum {self.a} + {self.b} should be more than {self.c}')
        if self.a + self.c < self.b:
            raise ValueError(f'Sum {self.a} + {self.c} should be more than {self.b}')
        if self.b + self.c < self.a:
            raise ValueError(f'Sum {self.b} + {self.c} should be more than {self.a}')
