from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b
        self.name = 'Rectangle'
        Rectangle.error(self)

    def rectangle_area(self):
        self.area = self.a * self.b
        return self.area

    def rectangle_perimeter(self):
        self.perimeter = (self.a + self.b) * 2
        return self.perimeter

    def error(self):
        if self.a <= 0:
            raise ValueError(f'Side a must be greater than 0, got {self.a}')
        if self.b <= 0:
            raise ValueError(f'Side a must be greater than 0, got {self.b}')
        if self.a == self.b:
            raise ValueError(f"Sides don't have to be equal {self.a} != {self.b}")
