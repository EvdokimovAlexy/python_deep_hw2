# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

FILE = os.path.abspath('file.txt')


def split_path(path: str):
    path_only, t, file_name = path.rpartition('\\')
    file_name, t, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext


def main():
    print(split_path(FILE))


if __name__ == "__main__":
    main()
