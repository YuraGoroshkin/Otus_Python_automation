from src.figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        super().__init__()
        self.a = a

    def square_area(self):
        Square.area = self.a * 2
        return Square.area

    def square_perimeter(self):
        Square.perimeter = self.a * 4
        return Square.perimeter

    @staticmethod
    def add_area(value):
        return Square.area + value
