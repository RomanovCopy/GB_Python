# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна: a. принимать параметр желаемое конечное имя файлов desired_name. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере num_digits.
# c. принимать параметр расширение исходного файла source_ext . Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла target_ext.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории.

# Пример использования.

# На входе:


# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
# На выходе:


# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, n

import os

def rename_files(desired_name="", num_digits=3, source_ext="", target_ext="", name_range=None):
    
    # Путь к папке
    folder = "test_folder"
    
    # Проверяем существование папки, если не существует, создаем её
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Получаем список всех файлов в папке
    files = os.listdir(folder)
    
    # Отбираем файлы с указанным расширением
    files_to_rename = [f for f in files if f.endswith(f".{source_ext}")]
    
    # Сортируем файлы для упорядоченного переименования
    files_to_rename.sort()
    
    # Переименовываем файлы
    for i, filename in enumerate(files_to_rename):
        # Извлекаем оригинальное имя файла без расширения
        original_name = os.path.splitext(filename)[0]
        
        # Извлекаем часть оригинального имени по указанному диапазону
        if name_range:
            original_name_part = original_name[name_range[0]-1:name_range[1]]
        else:
            original_name_part = ""
        
        # Формируем новый порядковый номер с нужным количеством цифр
        file_counter = str(i + 1).zfill(num_digits)
        
        # Формируем новое имя файла
        new_name = f"{original_name_part}{desired_name}{file_counter}.{target_ext}"
        
        # Путь к исходному и новому файлу
        source_path = os.path.join(folder, filename)
        target_path = os.path.join(folder, new_name)
        
        # Переименовываем файл
        os.rename(source_path, target_path)

# Пример использования
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", name_range=[3, 6])



