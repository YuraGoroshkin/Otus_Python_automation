from src.figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        super().__init__()
        self.a = a
        self.name = 'Square'
        Square.error(self)

    def square_area(self):
        self.area = self.a * 2
        return self.area

    def square_perimeter(self):
        self.perimeter = self.a * 4
        return self.perimeter

    def error(self):
        if self.a <= 0:
            raise ValueError('ValueError')
