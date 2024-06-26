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