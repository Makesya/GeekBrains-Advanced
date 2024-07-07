"""Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений."""


class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def lenght(self):
        return 2 * (self.width + self.height)

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other):
        return Rectangle(self.width - other.width, self.height - other.height)

    def __str__(self) -> str:
        return f"=== Rectangle ===\nWidth: {self.width}\nHeight: {self.height}\nArea: {self.area()}\nLenght: {self.lenght()}"


if __name__ == "__main__":
    r1 = Rectangle(25, 15)
    r2 = Rectangle(12, 12)
    print(r1 + r2)
    print(r1 - r2)
