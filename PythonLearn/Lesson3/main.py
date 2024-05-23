from random import randint as r

from tomlkit import key

myArray = [2, 4, 6, 8, 10, 22]
myDict = {"key1": "value1", "key2": "value2"}

print(myArray[0])
print(myDict["key1"])

myArray.append(24)  # Добавляет элемент в конец списка
myArray.extend("Extend")  # Добавляет элементы в конец списка # type: ignore
myDict["key3"] = "value3"  # Добавляет элемент в конец словаря

print(myArray)
print(myDict)

myArray.pop(-2)  # Удаляет элемент из списка по индексу
myDict.pop("key2")  # Удаляет элемент из словаря по ключу

print(myArray)
print(myDict)

print(myArray.count(2))  # Возвращает количество элементов с заданным значением
print(myDict.get("key1"))
# Возвращает значение по ключу, если ключ не найден, то возвращается None

myArray.index(22)  # Возвращает индекс первого элемента с заданным значением
myDict.keys()  # Возвращает список ключей словаря
myDict.values()  # Возвращает список значений словаря
myDict.items()  # Возвращает список кортежей словаря
# myDict.clear()  # Очищает словарь
# myArray.clear()  # Очищает список
myArray.insert(1, 23)  # Вставляет элемент в список по индексу
myDict.update({"key4": "value4"})  # Обновляет словарь

"""
pop - удаляет элемент из списка по индексу
remove - удаляет элемент из списка по значению
"""

print()
print(myArray)
print(myDict)


# Создаем список из 10 случайных чисел от 1 до 30
nList = [r(1, 30) for _ in range(10)]

print(nList)
sort_nList = sorted(nList)  # Сортируем список
sort_nList.reverse()  # Разворачиваем список
print(sort_nList)
print(sort_nList[::-1])  # Обратно разворачиваем список

xaero = dict(name="Alexar", age=25, city="Moscow")
xaero2 = {"name": "Alexar", "age": 25, "city": "Moscow"}

print(f"xaero: {xaero}\nxaero2: {xaero2}\nisIdentical: {xaero == xaero2}")

mDict = {f"{key}": value for key, value in zip(
    range(1, 10), range(10, 100, 3))}

print(mDict)
mDict.setdefault("default", 999)
print(mDict)
print(f"\n ")

for key, value in mDict.items():
    print(f"{key}: {value}")

long_lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."

llorem = set(long_lorem)
print(llorem)
llorem.add("812")  # Добавляет один элемент в множество
llorem.remove(" ")  # Удаляет один элемент из множества
llorem.discard(" ")  # Удаляет один элемент из множества, если он есть
llorem.update(["925"])  # Добавляет несколько элементов в множество
llorem.difference_update("U")  # Удаляет все элементы из множества
print(llorem)

print(5 in llorem)
print("q" in llorem)
