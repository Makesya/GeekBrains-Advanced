import datetime
import os


class MyStr(str):
    def __new__(cls, value):
        instance = super().__new__(cls, value)
        instance.created = datetime.datetime.now()
        instance.author = os.getlogin()
        return instance

    def info(self):
        return f"{self} was created at {self.created} by {self.author} "


if __name__ == "__main__":
    print(
        f"=== Programm started at {datetime.datetime.now().strftime('%H:%M')} ===")

    obj = MyStr("Hello, World!")

    print(obj.info())
    print(obj)
    print(obj.lower())
