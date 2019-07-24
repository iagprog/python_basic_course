# python with_args.py param1 param2 param3

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import easy
import normal


def print_help():
    print("help - getting help")
    print("mkdir <dir_name> - create directory")
    print("cp <file_name> - creates a copy of the specified file")
    print("rm <file_name> - deletes the specified file")
    print("cd <full_path or relative_path> - changes the current directory to the specified")
    print("ls - displays the full path of the current directory")


def make_dir():
    if not dir_name:
        print("Specify the directory name as the second parameter.")
        return
    else:
        easy.create_dir(dir_name)


def cp_file():
    if not dir_name:
        print("Specify the directory name as the second parameter.")
        return
    else:
        easy.copy_file(dir_name)

# Deletes directory or file


def rm_file():
    if not dir_name:
        print("Specify the directory name as the second parameter.")
        return
    else:
        confirm_rm = input(f"You are ready to delete directory/file '{dir_name}'. Are you sure? (Y/N) ")
        if confirm_rm == 'y' or confirm_rm == 'Y':
            if os.path.isfile(dir_name):
                try:
                    os.remove(dir_name)
                except OSError:
                    print(f"Can't delete file {dir_name}")
                else:
                    print(f"Successfully deleted file '{dir_name}'.")
            else:
                easy.delete_dir(dir_name)


def cd_dir():
    if not dir_name:
        print("Specify the directory name as the second parameter.")
        return
    else:
        normal.change_dir(dir_name)


def ls_dir():
    try:
        full_path = os.getcwd()
        print("Full path of the current directory: ", full_path)
    except OSError:
        print("Can't show full path of the current directory.")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": cp_file,
    "rm": rm_file,
    "cd": cd_dir,
    "ls": ls_dir
}


try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Invalid key specified.")
        print("Provide help key for help.")
