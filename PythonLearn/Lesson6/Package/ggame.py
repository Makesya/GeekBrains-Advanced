from random import randint
from sys import argv

__all__ = ["choiseNumber"]


def play(lowLimit: int = 1, upLimit: int = 10, attemps: int = 5) -> bool:
    """Это функция для угадывания числа

    Args:
        lowLimit (int): Нижняя граница диапазона
        upLimit (int): Верхняя граница диапазона
        attemps (int): Число попыток

    Returns:
        bool: Возвращает True если угадали и False если проиграли
    """
    number = randint(lowLimit, upLimit)
    print(
        f"Число загадано в диапазоне от {lowLimit} до {upLimit} попробуйте его отгадать!")
    for i in range(attemps):
        num = input(f"Осталось попыток: {attemps} \nВведите число: ")
        if int(num) == number:
            print("Вы угадали!")
            return True
        else:
            if attemps == 1:
                print("Вы проиграли")
                return False
            attemps -= 1
            if int(num) > number:
                print("Загаданное число меньше")
            else:
                print("Загаданное число больше")

    return False


if __name__ == "__main__":
    print(argv)
    if len(argv) == 4:
        play(int(argv[1]), int(argv[2]), int(argv[3]))
    else:
        play()
