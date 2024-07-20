# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

# Создайте файл __init__.py и запишите в него все функции:
# get_dir_size,
# save_results_to_json,
# save_results_to_csv,
# save_results_to_pickle, traverse_directory.


code_to_write='''
import os
import json
import csv
import pickle

def get_dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)
    return total_size

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

def save_results_to_json(results, json_file):
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=4)

def save_results_to_csv(results, csv_file):
    keys = results[0].keys()
    with open(csv_file, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)

def save_results_to_pickle(results, pickle_file):
    with open(pickle_file, 'wb') as f:
        pickle.dump(results, f)
'''
    
with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
