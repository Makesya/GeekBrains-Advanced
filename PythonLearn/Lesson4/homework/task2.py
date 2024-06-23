'''
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

Пример использования.
На входе:


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
На выходе:


{1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
'''


def key_params(*args, **kwargs):
    params = {}
    for key, value in kwargs.items():
        if type(value) == list or type(value) == dict:
            params[str(value)] = key
        else:
            params[value] = key
    return params


# Пример использования
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)

# {'1': 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
