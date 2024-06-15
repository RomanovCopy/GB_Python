# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.

# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.

# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.

# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.

# Пример

# На входе:


# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
# На выходе, например, один из допустимых вариантов может быть таким:


# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}

items = {
    "спальник": 1.5,
    "палатка": 3.2,
    "термос": 0.6,
    "карта": 0.1,
    "фонарик": 0.3,
    "котелок": 0.8,
    "еда": 2.5,
    "одежда": 1.7,
    "обувь": 1.2,
    "нож": 0.2
}
max_weight = 7.0


my_list = [(key, value) for key, value in items.items()]
best_variant = []
best_weight = 0
backpack={}
for i in range(len(my_list)):
    variant = [my_list[i]]
    w = my_list[i][1]
    if w > max_weight:
        continue
    for j in range(len(my_list)):
        if j > i:
            if w + my_list[j][1] <= max_weight:
                w += my_list[j][1]
                variant.append(my_list[j])
    if w <= max_weight and w > best_weight:
        best_weight = w
        best_variant = variant

if best_variant:
    backpack = {key: value for key, value in best_variant}

 


