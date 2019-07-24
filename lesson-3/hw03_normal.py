# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    a1 = 1
    a2 = 1
    i = 2
    res = []
    while i < m:
        s = a1 + a2
        a1 = a2
        a2 = s
        i += 1
        if i >= n:
            res.append(s)
    return res


print(fibonacci(5, 8))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = len(origin_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func_object, iterable):
    res = []
    for n in iterable:
        if func_object(n):
            res.append(n)
    return res


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a, b, c, d):
    x1 = (a[0] + c[0]) / 2
    x2 = (b[0] + d[0]) / 2
    y1 = (a[1] + c[1]) / 2
    y2 = (b[1] + d[1]) / 2
    if x1 == x2 and y1 == y2:
        return True
    else:
        return False


print(is_parallelogram((2, 4), (-3, 7), (-6, 6), (-1, 3)))


