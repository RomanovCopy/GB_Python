﻿# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

my_dict={
    "user1":("thing1", "thing2", "thing3", "thing4"),
    "user2":("thing3", "thing5", "thing2", "thing6"),
    "user3":("thing6", "thing4", "thing2", "thing5")
    }

all_users=set(my_dict["user1"]).intersection(set(my_dict["user2"]).intersection(set(my_dict["user3"])))

# unique_users=

print(all_users)
