
class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def info(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius ** 2

    def info(self):
        return f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area()}{self.unit}"


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * self.__side_a * self.__side_b

    def info(self):
        return f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {self.calculate_area()}{self.unit}"



circle1 = Circle(2)
circle2 = Circle(3)
triangle1 = RightTriangle(5, 8)
triangle2 = RightTriangle(3, 4)
triangle3 = RightTriangle(6, 9)


shapes = [circle1, circle2, triangle1, triangle2, triangle3]


for shape in shapes:
    print(shape.info())
