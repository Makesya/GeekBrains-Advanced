'''
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
На входе:
text = 'Hello world. Hello Python. Hello again.'
На выходе:
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
'''

from collections import Counter
text = 'This is a sample text without repeating words.'
# Удаление цифр
text = ''.join([i for i in text if not i.isdigit()])
# Удаление знаков препинания
words = text.replace('.', ' ').replace(
    ',', ' ').replace("'", " ").replace('!', " ").replace("?", " ").lower().split()
# Сортировка массива в обратном алфавиьтном порядке
words.sort(reverse=True)


c = Counter(words)
print(c.most_common(10))
