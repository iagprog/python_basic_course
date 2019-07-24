# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


def create_dir(dir_name):
    try:
        os.mkdir(os.path.join(os.getcwd(), dir_name))
    except FileExistsError:
        print(f"Can't create directory '{dir_name}'.")
    else:
        print(f"Successfully created directory '{dir_name}'.")


def delete_dir(dir_name):
    try:
        os.rmdir(os.path.join(os.getcwd(), dir_name))
    except OSError:
        print(f"Can't delete directory '{dir_name}'.")
    else:
        print(f"Successfully deleted directory '{dir_name}'.")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir():
    files = os.listdir(os.getcwd())
    print(files)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file(file_name):
    file_no_ext, file_ext = os.path.splitext(file_name)
    new_file = file_no_ext + '-copy' + file_ext
    try:
        shutil.copy(file_name, new_file)
    except OSError:
        print(f"Can't copy file '{file_name}'.")
    else:
        print(f"Successfully copied '{file_name}'.")


if __name__ == "__main__":
    while True:
        print("1 - Create dir1-dir9.")
        print("2 - Delete dir1-dir9.")
        print("3 - List of folders in current directory.")
        print("4 - Copy current file.")
        print("5 - Exit.")
        mode = input("Enter mode: ")
        if mode == '1':
            for i in range(1, 10):
                create_dir(f"dir{i}")
        elif mode == '2':
            for i in range(1, 10):
                delete_dir(f"dir{i}")
        elif mode == '3':
            list_dir()
        elif mode == '4':
            copy_file(__file__)
        elif mode == '5':
            break
