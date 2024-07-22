# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, 
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

# a, b, c (целые числа) - коэффициенты квадратного уравнения.

# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах 
# вычислений для каждой строки данных из CSV-файла.

# Пример

# На входе:


# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")

# with open("results.json", 'r') as f:
#     data = json.load(f)

# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

# print(len(data)==101)
# На выходе:


# True
# True
# Формат JSON файла определён следующим образом:

# [
#     {"parameters": [a, b, c], "result": result},
#     {"parameters": [a, b, c], "result": result},
#     ...
# ]


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

# file_name = 'data.csv'
# rows = random.randint(100, 1000)  # генерируем случайное количество строк от 100 до 1000
# generate_csv_file(file_name, rows)    



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

# пример использования функции
# a = 1
# b = -3
# c = 2
# roots = find_roots(a, b, c)
# print(roots)


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)