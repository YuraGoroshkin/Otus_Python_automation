from src.figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        super().__init__()
        self.a = a
        self.name = 'Square'
        Square.error(self)

    @property
    def area(self):
        return self.a * 2

    @property
    def perimeter(self):
        return self.a * 4

    def error(self):
        if self.a <= 0:
            raise ValueError(f'Side a must be greater than 0, got {self.a}')
