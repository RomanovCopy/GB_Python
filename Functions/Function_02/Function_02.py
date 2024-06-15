#  Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def my_func(line: str):
    unicodes = sorted([ord(line[i]) for i in range(len(line))], reverse=True)
    return unicodes


print(my_func("Romanov"))