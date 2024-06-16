# Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

from operator import index


def my_func(numbers, index_1: int, index_2: int):
    index_min = min([index_1, index_2])
    index_max = max([index_1, index_2])
    length = len(numbers)
    if length > 2:
        if index_min < 0 or index_min > length:
            index_min = 0
        if index_max < 0 or index_max > length:
            index_max = len(numbers)
        return sum(numbers[index_min+1:index_max])
    else:
        return 0


print(my_func([1, 2, 3, 4, 5, 6, 7, 8], 2, 10))