# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

import array


def my_func(line: str):
    array = sorted(line.split())
    my_list = [(i+1, array[i]) for i in range(len(array))]
    max_length = max(len(s) for _, s in my_list)
    [print(f"{t[0]} {t[1].rjust(max_length)}") for t in my_list]


my_func("Romanov Sergey Mihailovich 1971 2024 ")
