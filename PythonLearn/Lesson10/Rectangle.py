class Rectangle:
    def __init__(self, width, height=None):
        if not height:
            self.width = width
            self.height = width
        else:
            self.width = width
            self.height = height

    def area(self):
        return self.width * self.height

    def lenght(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.height == self.width:
            return f"=== Square ===\nLength: {self.width}\nArea: {self.area()}\nLenght: {self.lenght()}"
        return f"=== Rectangle ===\nWidth: {self.width}\nHeight: {self.height}\nArea: {self.area()}\nLenght: {self.lenght()}"


box = Rectangle(11)
print(box)
