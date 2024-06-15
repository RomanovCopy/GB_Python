# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def my_func(line: str):
    numbers = (int(line.split()[0]), int(line.split()[1]))
    my_dict = {chr(i): i for i in range(min(numbers), max(numbers))}
    return my_dict


print(my_func("200 250"))
