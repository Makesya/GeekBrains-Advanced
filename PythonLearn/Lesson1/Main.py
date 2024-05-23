text = input('Введите текст: ')
if text.isdigit():
    print(f'{bin(int(text))}\n{oct(int(text))}\n{hex(int(text))}')
else:
    if text.isascii():
        print(f'{text} - Написан в ASCII')
    else:
        print(f'{text} - Написан в Unicode')
