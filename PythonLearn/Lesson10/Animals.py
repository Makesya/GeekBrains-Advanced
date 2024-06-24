class Animal():

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_info(self):
        return {"name": self.get_name()}


class Cat(Animal):
    def __init__(self, name, color, age):
        super().__init__(name)
        self.__color = color
        self.__age = age
        self.__type = "cat"

    def get_info(self):
        return {"type": self.__type, "name": self.get_name(), "color": self.__color, "age": self.__age}


class Bird(Animal):
    def __init__(self, name, color, age, speed):
        super().__init__(name)
        self.__color = color
        self.__age = age
        self.__speed = speed
        self.__type = "bird"

    def get_info(self):
        return {"type": self.__type, "name": self.get_name(), "color": self.__color, "age": self.__age, "speed": self.__speed}


class Camel(Animal):
    def __init__(self, name, color, age, weight):
        super().__init__(name)
        self.__color = color
        self.__age = age
        self.__weight = weight
        self.__type = "camel"

    def get_info(self):
        return {"type": self.__type, "name": self.get_name(), "color": self.__color, "age": self.__age, "weight": self.__weight}


if __name__ == "__main__":
    cat = Cat("Barsik", "black", 5)
    bird = Bird("Kesha", "white", 2, 30)
    camel = Camel("Vasya", "green", 3, 1000)

    print(cat.get_info())
    print(bird.get_info())
    print(camel.get_info())
