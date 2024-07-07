import typing


class Archive(object):
    _instance = None
    archive_text: typing.List[str] = []
    archive_number: typing.List[typing.Union[int, float]] = []

    @staticmethod
    def __new__(cls, text: str, number: typing.Union[int, float], *args):
        if cls._instance is None:
            cls._instance = super(Archive, cls).__new__(cls)
            cls.archive_text = []
            cls.archive_number = []
        cls.archive_text.append(text)
        cls.archive_number.append(number)
        return cls._instance

    def __init__(self, text: str, number: typing.Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f"Archive('{self.text}', {self.number})"
