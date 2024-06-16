# Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def my_func(names, salary_rates, awards):
    my_dict={}
    for name, salary_rate, award in zip(names,salary_rates,awards):
        my_dict[name]=salary_rate+(salary_rate/100*award)
    return my_dict

print(my_func(["User1", "User2", "User3"],[1500, 1300, 2000],[10.15, 15.0, 12.7]))
    