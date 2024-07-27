# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.


import os
import sys
import logging
from collections import namedtuple

# Определение структуры данных
FileInfo = namedtuple('FileInfo', 'name extension is_directory parent_directory')

def gather_directory_info(directory_path):
    # Проверка, что путь существует и является директорией
    if not os.path.exists(directory_path):
        logging.error(f"Path does not exist: {directory_path}")
        return []

    if not os.path.isdir(directory_path):
        logging.error(f"Path is not a directory: {directory_path}")
        return []

    info_list = []
    for root, dirs, files in os.walk(directory_path):
        # Добавляем информацию о каталогах
        for dir_name in dirs:
            parent_dir = os.path.basename(root)
            info = FileInfo(
                name=dir_name,
                extension='',
                is_directory=True,
                parent_directory=parent_dir
            )
            logging.info(f"Directory found: {info}")
            info_list.append(info)
        
        # Добавляем информацию о файлах
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            parent_dir = os.path.basename(root)
            info = FileInfo(
                name=name,
                extension=extension[1:],  # Убираем точку из расширения
                is_directory=False,
                parent_directory=parent_dir
            )
            logging.info(f"File found: {info}")
            info_list.append(info)

    return info_list

def main():
    # Настройка логирования
    logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        return

    directory_path = sys.argv[1]
    gather_directory_info(directory_path)

if __name__ == "__main__":
    main()
