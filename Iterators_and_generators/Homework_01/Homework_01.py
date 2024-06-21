# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Пример использования.
# На входе:





file_path="/home/user/docs/my.file.with.dots.txt"
# file_path = "C:/Users/User/Documents/example.txt"
# file_path = 'file_in_current_directory.txt'
# На выходе:


# ('C:/Users/User/Documents/', 'example', '.txt')




def get_file_info(file_path):
    if isinstance(file_path, str) and len(file_path)>0:
        array=file_path.split('/')
        length=len(array)
        *_,name = array
        ext=f".{name.split('.')[len(name.split('.'))-1]}"
        name='.'.join( name.split('.')[:-1])
        path=""
        if len(array)>1:
            path=f"{'/'.join(map(str,array[:-1] ))}/"
    return (path,name,ext)
    
print( get_file_info(file_path))