import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

print("Задача-1.")
fruits = ["яблоко", "банан", "киви", "арбуз"]
print("Исходный список: ", fruits)
i = 0
while i < len(fruits):
    print('{}.{:>7}'.format(i+1, fruits[i]))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("Задача-2.")
L1 = []
L2 = []
for i in range(10):
    num = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    L1.append(num)
    L2.append(num2)
print("Исходный список 1: ", L1)
print("Исходный список 2: ", L2)
for a in L2:
    for b in L1:
        if a == b:
            L1.remove(a)
print(L1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("Задача-3.")
L1 = []
for i in range(10):
    num = random.randint(-10, 10)
    L1.append(num)
L2 = []
print("Исходный список: ", L1)
for a in L1:
    if a % 2 == 0:
        L2.append(a/4)
    else:
        L2.append(a*2)
print("Результат: ", L2)

