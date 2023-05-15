class Figure:
    def __init__(self, name: str = None):
        self._perimeter = None
        self._area = None
        self.name = name

    def add_area(self, other_obj):
        if isinstance(other_obj, Figure):
            return self.area + other_obj.area
        else:
            raise ValueError(f'Object {other_obj} is not a Figure')

    @property
    def perimeter(self) -> int:
        return self._perimeter

    @property
    def area(self) -> int:
        return self._area
