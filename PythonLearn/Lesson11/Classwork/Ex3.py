class Archive:
    deletedArchives = {}
    """
    Класс для архивирования данных

    Атрибуты:
        digit - цифра
        string - строка

    Методы:
        __init__(self, number: int, text: str)
    """

    def __init__(self, number: int, text: str):
        self.digit = number
        self.text = text
        if self.digit in Archive.deletedArchives:
            Archive.deletedArchives[self.digit].append(self.text)
        else:
            Archive.deletedArchives[self.digit] = [self.text]

    def __str__(self):
        """  
        Информационное представление объекта (для пользователя)
        """
        return f"=== Archive {self.digit} ===\n{self.text}"

    def __repr__(self) -> str:
        """ 
        Информационное представление объекта (для отладки)
        """
        return f"ID: {self.digit} \nValue: {self.text}"


if __name__ == '__main__':
    ar = Archive(1, 'text1')

    print(f"Repr method: {repr(ar)}")
    print(f"Str method: {str(ar)}")
