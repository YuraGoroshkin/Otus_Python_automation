class Figure:
    def __init__(self, name: str = None):
        self._perimeter = None
        self._area = None
        self.name = name

    @property
    def perimeter(self) -> int:
        return self._perimeter

    @property
    def area(self) -> int:
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @perimeter.setter
    def perimeter(self, value):
        self._perimeter = value
