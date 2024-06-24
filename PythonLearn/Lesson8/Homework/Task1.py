
import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})

        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})

    return results


def get_dir_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)

    return total_size


def save_results_to_json(results, file_name):
    with open(file_name, 'w') as f:
        json.dump(results, f, indent=4)


def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)


if __name__ == '__main__':
    directory = 'PythonLearn/Lesson8'
    results = traverse_directory(directory)
    save_results_to_json(results, 'results.json')
    save_results_to_csv(results, 'results.csv')
    save_results_to_pickle(results, 'results.pickle')
