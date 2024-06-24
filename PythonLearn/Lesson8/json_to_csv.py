from pathlib import Path
import json
import csv
import os
import sys


def convert_to_csv(file: Path):
    with open(file) as jfile:
        data = json.load(jfile)
    with open("PythonLearn/Lesson8/data.csv", "w") as cfile:
        writer = csv.writer(cfile, delimiter="-", lineterminator=";\n")
        for key, value in data.items():
            writer.writerow([key, value])


convert_to_csv("PythonLearn/Lesson8/data.json")
