class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        matching_numbers = [num for num in self.list1 if num in self.list2]

        if not matching_numbers:
            print("Совпадающих чисел нет.")
        else:
            print(f"Совпадающие числа: {matching_numbers}")
            print(f"Количество совпадающих чисел: {len(matching_numbers)}")


# Пример использования
list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
