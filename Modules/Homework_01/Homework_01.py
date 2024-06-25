# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.

# Пример использования На входе:


# date_to_prove = 15.4.2023
# На выходе:


# True
# На входе:


# date_to_prove = 31.6.2022
# На выходе:


# False

from datetime import datetime


def validate_date(date_string, date_format="%d.%m.%Y"):
# def validate_date(date_string, date_format="%Y-%m-%d"):
    """
    Проверяет, является ли введенная строка допустимой датой в заданном формате.

    Аргументы:
    date_string (str): Строка даты для проверки.
    date_format (str): Формат даты. По умолчанию "%Y-%m-%d".

    Возвращает:
    bool: True, если дата допустима, иначе False.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

# Пример использования:
date_string = "15.4.2023"
print(validate_date(date_string))  # Выведет: True
    
# date_string = "2024-06-18"
# print(validate_date(date_string))  # Выведет: True


invalid_date_string = "30.02.2024"
# invalid_date_string = "2024-02-30"
print(validate_date(invalid_date_string))  # Выведет: False
