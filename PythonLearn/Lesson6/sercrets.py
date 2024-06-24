def secrets(riddle: str, answers: list, attemps: int, trueAnswer: int) -> int:
    """Это функция для угадывания загадки

    Args:
        riddle (str): Загадка
        answers (list): Варианты ответов
        attemps (int, optional): Количество попыток. По умолчанию 5

    Returns:
        int: Возвращает номер попытки с которой угадали, либо 0 если проиграли
    """
    for i in range(attemps):
        print(f"======== Загадка ========")
        print(riddle)
        print(f"======== Варианты ответов ========")
        for j in range(len(answers)):
            print(f"{j + 1}. {answers[j]}")
        print(f"======== Кол-во попыток {attemps} ========")
        answer = input()
        attemps -= 1
        if int(answer) == trueAnswer:
            print("Вы угадали")
            return i + 1
        else:
            print("Неправильно")

    return 0


if __name__ == "__main__":
    print(secrets("Зимой и летом одним цветом?", [
          "Береза", "Ель", "Дуб", "Лиственница"], 5, 2))
