import re
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.

# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.

# Пример

# На входе:

# На выходе:


# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]



text = "Python 3.9 is the latest version of Python. It's awesome!"

text= text.replace('\''," ")
filtered_string = (re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', text)).lower()
elements=filtered_string.split()
my_dict={}
for element in elements:
    if element in my_dict:
        my_dict[element]+=1
    else:
        my_dict[element]=1
        
my_list=[(key, value) for key, value in my_dict.items()]
my_list=sorted(my_list, key=lambda x:x[1], reverse=True)

length=len(my_list)
start=-1
end=-1
if(length>0):
    
    for i in range(length-1):
        if(my_list[i][1]==my_list[i+1][1]):
            if start<0:
                start=i
            end=i+1
        else:
            if start>0:
                #сортируем срез внутри списка
                my_list[start:end] = sorted(my_list[start:end], key=lambda x: x[0], reverse=True)
                start=-1
                end=-1
    if start>=0:
        #если количество повторений одинаково
        my_list[start:end+1] = sorted(my_list[start:end+1], key=lambda x: x[0], reverse=True)
        start=-1
        end=-1
print(my_list[:10])
