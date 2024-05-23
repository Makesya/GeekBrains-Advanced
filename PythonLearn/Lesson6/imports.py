from sys import builtin_module_names, path
from random import randint as rnd, randrange as rrange
# print(sys)
# print(sys.builtin_module_names)
# print(*sys.path, sep="\n")

"""
import sys,random,os - так делать нельзя
"""


def randint_(*args):
    return "Не то что вы искали"


print(randint_(1, 10))  # Не то что вы искали
print(rnd(1, 10))

"""
Виды модулей:
    - Встроенные модули (имортируются через import)
    - Стороние модули (устанавливаются через pip & poetry)
    - Самописные модули (импортируется файл import)
"""
