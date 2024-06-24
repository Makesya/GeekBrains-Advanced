from math import pi


class Circle:

    """
    Класс окружности

    :param radius: Радиус окружности
    :type radius: int


    """

    def __init__(self, radius=10):
        self.radius = radius

    def area(self):
        """
        Возвращает площадь круга
        """
        return pi * (self.radius ** 2)

    def lenght(self):
        """
        Возвращает длину окружности
        """
        return 2 * pi * self.radius

    def __str__(self):
        return f"=== Circle {self.radius} ===\nRadius: {self.radius}\nArea: {self.area()}\nLenght: {self.lenght()}"


circle = Circle(5)
print(circle)
defaultCircle = Circle()
print(defaultCircle)
