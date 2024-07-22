

import csv
import json
import random
import math

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for _ in range(rows):
            data = [random.randint(100, 1000) for _ in range(3)]
            csvwriter.writerow(data)
            
            
def save_to_json(func):
    def wrapper(*args, **kwargs):
        file_name = args[0]  # �������� ��� CSV-����� �� ��������� �������
        data = []
        
        with open(file_name, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                a, b, c = map(int, row)  # ����������� ������ � ����� �����
                roots = func(a, b, c)  # �������� ������� find_roots
                result = {'a': a, 'b': b, 'c': c, 'roots': roots}
                data.append(result)

        with open('results.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    return wrapper    
    
    
    
@save_to_json
def find_roots(a, b, c):
    # ��������� ������������
    discriminant = b**2 - 4*a*c
    
    # ��������� ���� �������������
    if discriminant < 0:
        return None  # ��������� �� ����� ������
    elif discriminant == 0:
        root = -b / (2*a)
        return root  # ��������� ����� ���� ������
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2  # ��������� ����� ��� �����


