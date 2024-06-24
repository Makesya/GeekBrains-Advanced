import json


def convert_to_json(file):
    data = {}
    with open(file, 'r') as thisfile:
        for line in thisfile:
            data[line.split()[0]] = line.split()[1]

    with open("PythonLearn/Lesson8/data.json", 'w') as thisfile:
        # ensure_ascii=False - для корректного отображения русских букв
        json.dump(data, thisfile, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    convert_to_json("PythonLearn/Lesson8/data.txt")
