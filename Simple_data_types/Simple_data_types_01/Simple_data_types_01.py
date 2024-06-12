# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# Пример

# На входе:


# num = 255
# На выходе:


# Шестнадцатеричное представление числа: FF
# Проверка результата: 0xff

def dec_to_hex(num):
    hex_digits = "0123456789ABCDEF"
    
    if num == 0:
        return ""
    
    hex_num = ""
    while num > 0:
        remainder = num % 16
        hex_num = hex_digits[remainder] + hex_num
        num = num // 16
    
    return hex_num

num = int(input("Целое число: "))
hex_num = dec_to_hex(num)
print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", hex(num))