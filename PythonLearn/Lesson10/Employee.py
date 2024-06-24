from Person import Person


class Employee(Person):
    """Класс работника

        Аргументы:
            surname - фамилия
            name - имя
            lastname - отчество
            age - возраст
            id - идентификационный код
            access - сумма цифр идентификационного кода по модулю 7

        Методы:
            __init__(self, surname: str, name: str, lastname: str, age: int, id: int)
    """

    def __init__(self, surname: str, name: str, lastname: str, age: int, id: int):
        super().__init__(surname, name, lastname, age)
        if 100000 < id > 999999:
            raise ValueError("ID must be 6 digits long")
        self.__id = id
        self.__access = sum(map(int, str(id))) % 7

    def get_id(self):
        return self.__id

    def get_access(self):
        return self.__access

    def __str__(self):
        return f"{super().__str__()} {self.__id} {self.__access}"


if __name__ == "__main__":
    employee = Employee("Ivanov", "Ivan", "Ivanovich", 30, 123453)
    print(employee)
