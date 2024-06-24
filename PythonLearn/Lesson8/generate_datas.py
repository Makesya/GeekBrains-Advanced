from random import randint
import os


def generate_names(len: int = 6):
    chars = "qwertyuiopasdfghjklzxcvbnm"
    return "".join(chars[randint(0, chars.__len__() - 1)] for _ in range(len))


def generate_numbers(len: int = 5):
    return "".join(str(randint(0, 9)) for _ in range(len))


with open("PythonLearn/Lesson8/data.txt", "w") as f:
    for _ in range(100):
        f.write(f"{generate_names()} {generate_numbers()}\n")
