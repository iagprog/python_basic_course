import re
import math

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# inp_str = "5/6 + 4/7"

inp_str = input("Введите выражение:")
inp_tmp1 = inp_str.replace("- -", "+")
inp_tmp2 = inp_tmp1.replace("- +", "-")
inp_exp = inp_tmp2.replace("+ -", "-")
inp_exp = ' ' + inp_exp + ' '
pattern_x = "([0-9]+)/"
pattern_y = "/([0-9]+)"
pattern_k = "[' ']([+-]*[0-9]+)[' ']"
pattern_sign = "([+-])[' ']*[0-9]"

# Выделяем целые части, числители и знаменатели из строки

x = list(map(int, re.findall(pattern_x, inp_exp)))
y = list(map(int, re.findall(pattern_y, inp_exp)))
k = list(map(int, re.findall(pattern_k, inp_exp)))
op = re.findall(pattern_sign, inp_exp)

# Приводим к общему знаменателю целую и дробную части

all_y = 1
for i in y:
    all_y = all_y * int(i)
for i in range(len(k)):
    k[i] *= all_y
for i in range(len(x)):
    for j in range(len(y)):
        if i != j:
            x[i] *= y[j]

# Склеиваем числитель дроби с ее знаком

for i in range(len(x)):
    if i < len(op):
        x[i] = int(op[i]+str(x[i]))

# Считаем результат операций, выделяем целую часть, сокращаем дробь

all_x = sum(x)+sum(k)
res_x = abs(all_x) % all_y
gcd_xy = math.gcd(res_x, all_y)
if all_x < 0:
    integer_part_fraction = all_x + res_x
else:
    integer_part_fraction = all_x - res_x
res_n = integer_part_fraction / all_y
print("Результат: {} {}/{}".format(int(res_n), int(res_x / gcd_xy), int(all_y / gcd_xy)))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))