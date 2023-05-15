from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b
        self.name = 'Rectangle'
        Rectangle.error(self)

    @property
    def rectangle_area(self):
        return self.a * self.b

    @property
    def rectangle_perimeter(self):
        return (self.a + self.b) * 2

    def error(self):
        if self.a <= 0:
            raise ValueError('ValueError')
        if self.b <= 0:
            raise ValueError('ValueError')
        if self.a == self.b:
            raise ValueError('ValueError')
