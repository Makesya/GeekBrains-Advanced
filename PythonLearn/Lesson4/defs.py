import random


COUNTER = 0


def printArgs(a, b, c, *args):
    print(f"a = {a}, b = {b}, c = {c}, other = {args}")


def quadrant_eqalitons(a: int | float, b: int | float, c: int | float) -> list:
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.

    Parameters:
    a (int | float): Coefficient of x^2
    b (int | float): Coefficient of x
    c (int | float): Constant term

    Returns:
    list: A list of real roots of the quadratic equation. Returns an empty list if no real roots exist.
    """
    d = b**2 - 4 * a * c
    if d < 0:
        return []
    elif d == 0:
        return [-b / (2 * a)]
    else:
        return [(-b - d**0.5) / (2 * a), (-b + d**0.5) / (2 * a)]


def only_posArgs(args, /):
    """
    Эта функция принимает только позиционные аргументы
    """
    print(args)  # only_posArgs(123)


def only_kwArgs(*, username: str, password: str, email: str):
    """
    Эта функция принимает только ключевые аргументы
    """
    print(f"{username = }, {password = }, {email = }")  # only_kwArgs(username="Vasya")


def func_args_kwargs(*args, **kwargs):
    """
    Processes both positional and keyword arguments.

    This function prints the positional arguments and keyword arguments it receives.

    Args:
    *args: Variable length argument list.
    **kwargs: Arbitrary keyword arguments.

    Examples:
    func_args_kwargs(1, 2, 3, username="Vasya", password="123456", email="vasya@mail.ru")
    """
    print(f"{args = }")
    print(f"{kwargs = }")


def increment():
    """
    Increments the global counter by 1 and returns the new value.

    This function modifies the global variable `COUNTER` by incrementing its value by 1 each time the function is called.
    It then returns the incremented value.

    Returns:
        int: The incremented value of the global variable `COUNTER`.
    """
    global COUNTER
    COUNTER += 1
    return COUNTER


# func_args_kwargs(1, 2, 3, 4, 5, username="Vasya",
#                  password="123456", email="vasya@mail.ru")

for i in range(random.randint(1, 30)):
    increment()

print(f"{COUNTER = }")

'''
chr() - Функция возвращает символ по его ASCII коду
ord() - Функция возвращает ASCII код символа
'''

print(ord("の"))
print(chr(12398))

globals()  # Возвращает словарь глобальных переменных

locals()  # Возвращает словарь локальных переменных

vars()  # Возвращает словарь глобальных и локальных переменных
