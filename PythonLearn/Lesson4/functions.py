a = 42
print(type(a), id(a))  # Принт двух функций сразу
print(type(id))  # В функцию можно передавать другие функции

very_bad_programming_style = sum  # Так делать не надо
print(very_bad_programming_style([1, 3, 2, 4, 1, 2, 3, 4, 1, 2, 7]))
