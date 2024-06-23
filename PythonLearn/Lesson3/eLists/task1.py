'''
Задание №1 Вручную создайте список с целыми числами, которые повторяются. 
Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.


*Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
'''

customNums = [1, 3, 1, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 1, 2, 4, 5]
dontRepeatSet = list(set(customNums))
dontRepeatList = []
for el in customNums:
    if el not in dontRepeatList:
        dontRepeatList.append(el)

print(f'''
      {customNums = }
      {dontRepeatSet = }
      {dontRepeatList = }
      ''')
