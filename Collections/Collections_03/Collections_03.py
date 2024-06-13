# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях


line = input("Введите строку: ")

if line.isdigit() and int(line) > 0:
    print(f"{line} -> Целое положительное число: {int(line)}")
elif line.replace(".", "", 1).replace("-", "", 1).isdigit() and "." in line:
    print(f"{line} -> Вещественное число: {float(line)}")
elif any(s.isupper() for s in line):
    print(f"Заглавная буква в строке: {line.lower()}")
else:
    print(line.lower())


# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (23, 23.5, "string_line")

my_dict = {}
for element in my_tuple:
    key = type(element).__name__
    if key in my_dict:
        my_dict[key].append(element)
    else:
        my_dict[key] = [element]
print(my_dict)