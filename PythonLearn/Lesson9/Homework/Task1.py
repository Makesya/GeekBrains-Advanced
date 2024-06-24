import random
import json
import csv


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(rows):
            writer.writerow([random.randint(100, 1000), random.randint(
                100, 1000), random.randint(100, 1000)])


def save_to_json(func):
    def wrapper(*args, **kwargs):
        data = []
        with open(args[0], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data.append({'parameters': [a, b, c], 'result': result})
        with open('results.json', 'w') as f:
            json.dump(data, f, indent=4)
    return wrapper


@save_to_json
def find_roots(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        return -b/(2*a)
    else:
        return (-b + delta**0.5)/(2*a), (-b - delta**0.5)/(2*a)
