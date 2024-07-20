# ���� ������ - �������� ���������, ������� ��������� �� ���� ���������� � ���������� ������� ��� ���������� � ��� ��������� ����������. 
# ���������� ������ ������ ���� ��������� � ���������� ��������: JSON, CSV � Pickle. ������ ��������� ������ ��������� ��������� ����������:

# ���� � ����� ��� ����������: ���������� ���� � ����� ��� ����������. ��� �������: ��� ���� ��� ����������. 
# ������: ��� ������ - ������ � ������, ��� ���������� - ������, �������� ��� ��������� ����� � ���������� � ������. ������ ������:

# ��� �������� �������� (��� ������, ��� � ����������) ������� ������������ ����������.

# ��� ������ ��������� �� ������ � ������.

# ��� ����������, ������ �� �������, ������ ������ ���� ������ � ����������, ����������� ������ ������ ����������, � ��������� ����������.

# ��������� ������ ������������ ����������� ����� ����������, ����� ������ ��� ��������� �������.

# ���������� ������ ���� ��������� � ���� ��������: JSON, CSV � Pickle. ������� ������ ������ ���� �����������.

# ��� ������ �������� ������� �� ������ ������������ ������ os.

# ��� ���������� �������� ������� traverse_directory(directory), ������� ����� ��������� ����� ���������� � ���������� ���������� � ���� ������ ��������. 
# ����� ����� ���������� ������ ���� ��������� � ���� ��������� ������ (JSON, CSV � Pickle) � ������� ������� save_results_to_json, save_results_to_csv � save_results_to_pickle.

# ����� ����������� � ������ results � ��� �������, � ������� ��� ����������� ��� ����������� ������ ����������. ��� ���� ������� ����������� �����, � ����� ����������.

# ��� ������� ����� (name � files), ������� ��������� ������ ���� � ����� (path = os.path.join(root, name)), � ����� ���������� ������ ����� (size = os.path.getsize(path)). 
# ���������� � ����� ����������� � ������ results � ���� ������� {'Path': path, 'Type': 'File', 'Size': size}.

# �����, ��� ������ ���������� (name � dirs), ����� ��������� ������ ���� � ���������� (path = os.path.join(root, name)), � ���������� ������� get_dir_size(path), 
# ����� �������� ������ ���� ���������� � ������ �� �����������. ���������� � ���������� ����������� � ������ results � ���� ������� {'Path': path, 'Type': 'Directory', 'Size': size}.

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

directory = 'E:\\PicToMy\\001'
results = traverse_directory(directory)

save_results_to_json(results, 'results.json')
save_results_to_csv(results, 'results.csv')
save_results_to_pickle(results, 'results.pickle')