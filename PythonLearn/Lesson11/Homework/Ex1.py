class MyStr(str):

    def __new__(cls, value, author):
        import datetime
        instance = super().__new__(cls, value)
        instance.author = author
        instance.value = value
        instance.time = datetime.datetime.now()
        return instance

    def __str__(self) -> str:
        return f"{self.value} (Автор: {self.author}, Время создания: {self.time.strftime('%Y-%m-%d %H:%M')})"

    def __repr__(self) -> str:
        return f"MyStr{self.value, self.author}"
