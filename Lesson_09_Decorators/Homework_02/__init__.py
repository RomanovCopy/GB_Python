

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
        file_name = args[0]  # получаем имя CSV-файла из аргумента функции
        data = []
        
        with open(file_name, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                a, b, c = map(int, row)  # преобразуем строки в целые числа
                roots = func(a, b, c)  # вызываем функцию find_roots
                result = {'a': a, 'b': b, 'c': c, 'roots': roots}
                data.append(result)

        with open('results.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    return wrapper    
    
    
    
@save_to_json
def find_roots(a, b, c):
    # вычисляем дискриминант
    discriminant = b**2 - 4*a*c
    
    # проверяем знак дискриминанта
    if discriminant < 0:
        return None  # уравнение не имеет корней
    elif discriminant == 0:
        root = -b / (2*a)
        return root  # уравнение имеет один корень
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2  # уравнение имеет два корня


