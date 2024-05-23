from random import randint as r

'''
map - применяет функцию к каждому элементу списка
filter - применяет функцию к каждому элементу списка и возвращает только те элементы, которые функция вернула True
reduce - применяет функцию к каждому элементу списка и возвращает одно значение
'''

hello_words = ["Привет", "Здарова", "Приветствую"]

# Return [привет, здарова, приветствую]
toLower = list(map(lambda x: x.lower(), hello_words))
# Return [ПРИВЕТ, ЗДАРОВА, ПРИВЕТСТВУЮ]
toUpper = list(map(lambda x: x.upper(), hello_words))

# Список из 15 случайных чисел от -10 до 10
int_list = [r(-10, 10) for _ in range(15)]
print(int_list)

# Список из положительных чисел
positive = list(filter(lambda x: x > 0, int_list))
print(positive)

# Список из четных чисел
divide_by_2 = list(filter(lambda x: x % 2 == 0, int_list))
print(divide_by_2)


employees = [{
    "name": "John Doe",
    "salary": 50000,
    "datebirth": "1990-01-01",
}, {
    "name": "Jane Smith",
    "salary": 60000,
    "datebirth": "1985-05-15"
}, {
    "name": "Alice Johnson",
    "salary": 55000,
    "datebirth": "1992-07-23"
}]

print(f"Worker with max salary: {max(employees, key=lambda x: x['salary'])}")
print(f"Wasted salary: {sum(map(lambda x: x['salary'], employees))}")

print()

SIZE = 11


def func(a, b, c):
    x = a+b
    print(locals())
    z = x+c
    print(locals())
    return z


print(func(1, 2, 3))
