from pathlib import Path
import json
import os
import sys


def write_to_json(path: Path):
    if os.path.exists(path):
        with open(path, "r") as file:
            users = json.load(file)
    else:
        users = {str(level): {} for level in range(1, 7 + 1)}
    id_set = set(key for level in users.keys() for key in users[level].keys())
    while True:
        name = input("Введите имя: ")
        if not name:
            print("Завершение..")
            with open(path, "w") as file:
                json.dump(users, file)
            print("Запись завершена")
            break
        id = input("Введите ID: ")
        level = input("Введите уровень доступа: ")
        if int(level) <= 0 or int(level) >= 8:
            print("Уровень доступа может быть от 1 до 7\n")
            continue

        if id in id_set:
            print("Такой ID уже существует\n")
            print(f"Введите ID больше {max(id_set)}\n")

            continue
        id_set.update(id)
        users[level][id] = name

        print(users)


write_to_json(Path("users.json"))
