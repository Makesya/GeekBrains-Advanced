"""
Пример обмена значений переменных без использования временной переменной
"""

import time
import os
import sys
import functools
a = 1
b = 2

a, b = b, a

# print(a, b)

"""
Распакова и упаковка значений
"""

# values = input("Введите три числа: ").split()
# values = [v for v in values if v != " "]
# a, b, c, *args = values

# print(f"a: {a}, b: {b}, c: {c}\n Unpacked: {args}")


intList = [v*2 for v in range(50, 100) if v % 3 == 0]
print(intList)
print(*intList)  # Пример распаковки

"""
Присваивание нескольких переменных одновременно
"""

x, y, z = 4, 3, 2  # Хорошо
a = b = c = 0  # Тоже хорошо
q, w, e = {1, 2, 3}  # Не хорошо, тк неизвестно что за значения

"""
Множественное сравнение
"""

a = 12
b = 42
c = 33
if a > b > c:
    print("'b' is middle digit")
else:
    print("'a' is middle digit")

"""
Итераторы - это объекты, которые позволяют перебирать элементы коллекции данных, например список или кортеж. 

Функции:
    iter() - функция, которая создает итератор
    next() - функция, которая возвращает следующий элемент итератора
"""

a = 342
# iter(a)  # TypeError: 'int' object is not callable

data = [2, 4, 6, 8]
listIter = iter(data)
print(listIter)
"""
Итератор можно распковать
"""
print(*listIter)


# Добавляем путь к файлу в систему
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
os.chdir(script_dir)

with open("./mydata.bin", "rb") as f:
    for block in iter(functools.partial(f.read, 16), b""):
        print(block)

"""
next() - функция, которая возвращает следующий элемент итератора

Example: 
    next(iter(range(10)))
"""

data = [e for e in range(20) if e % 2 == 0]
liter = iter(data)
print(next(liter))  # 0
print(next(liter))  # 2
print(next(liter))  # 4
print(next(liter))  # 6
print(next(liter))  # 8
print(next(liter))  # 10
print(next(liter))  # 12
print(next(liter))  # 14
print(next(liter))  # 16
print(next(liter))  # 18
# print(next(liter))  # StopIteration


"""
Генераторы - это функции, которые возвращают итераторы.
"""

a = range(0, 10, 2)
print(f"{a = } {type(a)=} {a.__sizeof__()=} {len(a)=}")
b = range(0, 1_000_000, 2)
print(f"{b = } {type(b)=} {b.__sizeof__()=} {len(b)=}")


# #####################

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f"\n\n\n{len(x) = } {len(y) = }")
mult = (i + j for i in x if i % 2 != 0 for j in y if j % 2 == 0)
mult = list(mult)
print(*mult)
print(f"{len(mult) = }\n\n\n")

# #####################

eng_alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
rus_alphabet = [chr(i) for i in range(ord("а"), ord("я") + 1)]
print(*eng_alphabet)
print(*rus_alphabet)
print(f"{len(eng_alphabet) = } {len(rus_alphabet) = }\n\n\n")

# #####################


def factorial(n):
    """
    Standart function
    """
    result = []
    num = 1
    for i in range(1, n + 1):
        num *= i
        result.append(num)
    return result


"""
Генератор отличается от функции тем, что он сохраняет свое состояние между вызовами.
Используется ключевое слово yield, генераторы могут быть созданы с помощью функции.
Так же занимают меньше памяти, чем списки.
"""


def genFactorial(n):
    """
    Generator function
    """
    num = 1
    for i in range(1, n + 1):
        num *= i
        yield num


giter = iter(genFactorial(15))
for i, num in enumerate(giter, start=1):
    print(f"{i}! = {num:_}")
