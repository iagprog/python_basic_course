# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import easy
import os


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
    except OSError:
        print(f"Can't move to directory '{dir_path}'.")
    else:
        print(f"Successfully moved to directory '{dir_path}'.")


if __name__ == "__main__":
    while True:
        print("1 - Move to directory.")
        print("2 - List of folders in current directory.")
        print("3 - Delete directory.")
        print("4 - Create directory.")
        print("5 - Exit.")
        mode = input("Enter mode: ")
        if mode == '1':
            new_path = input("Enter directory path: ")
            change_dir(new_path)
        elif mode == '2':
            easy.list_dir()
        elif mode == '3':
            dir_name = input("Enter directory name: ")
            easy.delete_dir(dir_name)
        elif mode == '4':
            dir_name = input("Enter directory name: ")
            easy.create_dir(dir_name)
        elif mode == '5':
            break
