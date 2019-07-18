# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    c = 10 ** ndigits
    a = number * c
    b = int((a - int(a))*10)
    if b >= 5:
        a = int(a) + 1
    return a / c


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket = str(ticket_number)
    s = len(ticket)
    pos = s // 2
    first = ticket[0: pos]
    if s % 2:
        return "unlucky"
    last = ticket[pos:]
    sum1 = 0
    sum2 = 0
    for i in first:
        sum1 += int(i)
    for j in last:
        sum2 += int(j)
    if sum1 == sum2:
        return "lucky"
    return "unlucky"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
