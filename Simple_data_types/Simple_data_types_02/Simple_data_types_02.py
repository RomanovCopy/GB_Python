# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.

# Для проверки своего кода используйте модуль fractions.

# Пример

# На входе:
# frac1 = "1/2"
# frac2 = "1/3"

# На выходе:
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6
import fractions

frac1 = input("Дробь 1 :")
frac2 = input("Дробь 2 :")
frac_summ = ""
frac_mult = ""

frac1_1 = [int(x) for x in frac1.split('/')]
frac2_1 = [int(x) for x in frac2.split('/')]
fraction1 = fractions.Fraction(frac1_1[0], frac1_1[1])
fraction2 = fractions.Fraction(frac2_1[0], frac2_1[1])
if (frac1_1[1] == frac2_1[1]):
    # одинаковые знаменатели
    frac_summ = str(frac1_1[0]+frac2_1[0])+'/'+str(frac1_1[1])
else:
    # разные знаменатели
    numerator1 = frac1_1[0]*frac2_1[1]
    numerator2 = frac2_1[0]*frac1_1[1]
    denominator = frac1_1[1]*frac2_1[1]
    frac_summ = str(numerator1+numerator2)+'/'+str(denominator)

frac_mult = str(frac1_1[0]*frac2_1[0]) + '/'+str(frac1_1[1]*frac2_1[1])

print("Сумма дробей:", frac_summ)
print("Произведение дробей:", frac_mult)
print("Сумма дробей:", fraction1+fraction2)
print("Произведение дробей:", fraction1*fraction2)
