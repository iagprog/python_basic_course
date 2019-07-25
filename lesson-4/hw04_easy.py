import random

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print("Задание-1.")
old_list = [random.randint(-10, 10) for _ in range(10)]
print("Исходный список:\n", old_list)
new_list = [_ * _ for _ in old_list]
print("Новый список, заполненный квадратами элементов исходного списка:\n", new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print("Задание-2.")
fruits1 = ["apples", "bananas", "grapes", "lemons", "oranges"]
fruits2 = ["apples", "strawberries", "grapes", "lemons", "pomegranate"]
print("Первый список фруктов:\n", fruits1)
print("Второй список фруктов:\n", fruits2)
fruits = [x for x in fruits1 for y in fruits2 if x == y]
print("Список фруктов, присутствующих в обоих списках:\n", fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print("Задание-3.")
old_list = [random.randint(-10, 10) for _ in range(10)]
print("Исходный список: \n", old_list)
new_list = [x for x in old_list if x % 3 == 0 and x > 0 and x % 4 != 0]
print("Новый список (каждый элемент кратен 3, положительный, не кратен 4): \n", new_list)
