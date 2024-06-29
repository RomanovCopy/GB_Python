f = open('text_data.txt', 'r', encoding='utf-8')
print(f)
print(list(f))


# ➢ 'r' — открыть для чтения (по умолчанию)
# ➢ 'w' — открыть для записи, предварительно очистив файл
# ➢ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже
# существует
# ➢ 'a' — открыть для записи в конец файла, если он существует
# ➢ 'b' — двоичный режим
# ➢ 't' — текстовый режим (по умолчанию)
# ➢ '+' — открыты для обновления (чтение и запись)


f = open('text_data.txt', 'a', encoding='utf-8')
f.write('Окончание файла\n')
f.close()


# errors — используется только в текстовом режиме и определяет поведение в случае
# ошибок кодирования или декодирования. Рассмотрим несколько возможных
# вариантов параметра:
# ➢ 'strict' — вызывает исключение ValueError в случае ошибки. Работает как
# значение по умолчанию.
# ➢ 'ignore' — игнорирует ошибки кодирования. При этом игнорирование ошибок
# может привести к потере данных.
# ➢ 'replace' — вставляет маркер замены (например, '?') там, где есть
# некодируемые данные.
# ➢ 'namereplace' — при записи заменяет неподдерживаемые символы
# последовательностями \N{...}.

f = open('data.txt', 'wb')
f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()
f = open('data.txt', 'r', encoding='utf-8')
print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode
#byte 0xec in position 14: invalid continuation byte
f.close()
f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()

# newline — отвечает за преобразование окончания строки
# 7
# closefd — указывает оставлять ли файловый дескриптор открытым при закрытии
# файла
# opener — позволяет передать пользовательскую функцию для открытия файла.


with open('text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
print(f.write('Пока')) # ValueError: I/O operation on closed
#file.

with open('text_data.txt', 'r+', encoding='utf-8') as f1, open('bin_data', 'rb') as f2:
    print(list(f1))
    print(list(f2))
    

    
with (
open('text_data.txt', 'r+', encoding='utf-8') as f1,
open('bin_data', 'rb') as f2,
open('data.txt', 'r', encoding='utf-8',
errors='backslashreplace') as f3
):
    print(list(f1))
    print(list(f2))
    print(list(f3))
    

# read(n=-1) — читает n символов или n байт информации из файла. Если n
# отрицательное или не указана, читает весь файл. Попытка чтения будет даже в том
# случае, когда файл больше оперативной памяти.

with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')    


# Если прочитать файл до конца, повторные попытки чтения не будут вызывать
# ошибку. Метод будет возвращать пустую строку.


SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)    
        

# Для чтения текстового файла построчно используют метод readline.
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)
        

SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)
        

# Передача положительного числа в качестве аргумента задаёт границу для длины
# строки. Если строка короче границы, она возвращается целиком. А если больше, то
# возвращается часть строки заданного размера. При этом следующий вызов метода
# вернёт продолжение строки снова фиксированного размера или остаток до конца,
# если она короче.

with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')        
        

# Файл построчно попадает в переменную line. А для того чтобы избавиться от пустых
# строк отключили перенос строки в функции print.
#  Важно! Символ переноса строки сохранился в конце каждой строки.
# Если вам необходимо обработать строку без переносов, можно использовать
# срезы line[:-1] или метод замены line.replace('\n', '')


SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))     
    
        
# ➢ w — создаём новый пустой файл для записи. Если файл существует,
# открываем его для записи и удаляем данные, которые в нём хранились.
# ➢ x — создаём новый пустой файл для записи. Если файл существует, вызываем
# ошибку.
# ➢ a — открываем существующий файл для записи в конец, добавления данных.
# Если файл не существует, создаём новый файл и записываем в него.

# Метод write принимает на вход строку или набор байт в зависимости от того как вы
# открыли файл. После записи метод возвращает количество записанной
# информации.
text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')
    

# Метод не добавляет символ перехода на новую строку. Если произвести несколько
# записей, они “склеиваются” в файле.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing\
elit.',
'Consequatur debitis explicabo laboriosam sint suscipit\
temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia\
saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(line)
        print(f'{res = }\n{len(line) = }')
        

# Если каждая строка должна сохранятся в файле с новой строки, необходимо
# самостоятельно добавить символ переноса - \n
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing\
elit.',
'Consequatur debitis explicabo laboriosam sint suscipit\
temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia\
saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')
        


# В отличии от write этот метод ничего не возвращает.
        
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing\
elit.',
'Consequatur debitis explicabo laboriosam sint suscipit\
temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia\
saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
    
# Для того чтобы каждый элемент списка text сохранялся в файле с новой строки
# воспользовались строковым методом join. writelines не добавляет переноса между
# элементами последовательности


# Функция print по умолчанию выводит информацию в поток вывода. Обычно это
# консоль. Но можно явно передать файловый объект для печати в файл. Для этого
# надо воспользоваться ключевым параметром file.
    
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing\
elit.',
'Consequatur debitis explicabo laboriosam sint suscipit\
temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia\
saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)
        
# В отличии от методов записи в файл, функция print добавляет перенос строки.
# Кроме того ничто не мешает явно изменить параметр end функции.
        
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing\
elit.',
'Consequatur debitis explicabo laboriosam sint suscipit\
temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia\
saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)    
        

#Метод tell возвращает текущую позицию в файле.

text = ['Lorem ipsum dolor sit amet, consectetur adipisicing\
elit.',
'Consequatur debitis explicabo laboriosam sint suscipit\
temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia\
saepe totam velit?', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
print(f.tell()) # ValueError: I/O operation on closed file.



# Метод seek позволяет изменить положение “курсора” в файле.

# seek(offset, whence=0), где offset — смещение относительно опорной точки, whence -
# способ выбора опороной точки.
# ● whence = 0 - отсчёт от начала файла
# ● whence = 1 - отсчёт от текущей позиции в файле
# ● whence = 2 - отсчёт от конца файла

# 🔥 Важно! Значения 1 и 2 допустимы только для работы с бинарными
# файлами. Исключение seek(0, 2) для перехода в конец текстового файла.


last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing\
elit.',
'Consequatur debitis explicabo laboriosam sint suscipit\
temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia\
saepe totam velit?', ]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
    

# Метод truncate
# truncate(size=None) — метод изменяет размер файла. Если не передать значение в
# параметр size будет удалена часть файла от текущей позиции до конца. Метод
# возвращает позицию после изменения файла.
last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate())
# Если передать параметр size метод изменяет размер файла до указанного числа
# символов или байт от начала файла.
size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))
    

