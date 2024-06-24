class Person():

    def __init__(self,
                 surname: str = 'undefined',
                 name: str = 'undefined',
                 lastname: str = 'undefined',
                 age: int = 18):
        self.surname = surname
        self.name = name
        self.lastname = lastname
        self.__age = age

    def __str__(self):
        return f"{self.surname} {self.name} {self.lastname} {self.__age}"

    def birtday(self, years: int = 1):
        self.__age += years

    def full_name(self):
        return f"""{self.name} {self.surname} {self.lastname} {self.__age}"""

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    person = Person('Ivanov', 'Ivan', 'Ivanovich', 30)
    print(person)
    person.birtday(1)
    print(person.full_name())
    person.age = 40
    print(person.full_name())
