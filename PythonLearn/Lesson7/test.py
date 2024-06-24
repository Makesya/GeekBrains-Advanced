from sys import argv
import warnings

warnings.filterwarnings('ignore')


with open("PythonLearn/Lesson7/__init__.py", "r") as init_file:
    code = init_file.read()

function_names = [
    "def rename_files"
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")
