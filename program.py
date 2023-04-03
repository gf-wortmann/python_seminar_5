# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

x, y = input('enter 2 numbers: ').split()
x = int(x)
y = int(y)


def sum_recursive(a, b):
    if b == 0:
        return a
    else:
        a += 1
        return sum_recursive(a, b - 1)


print(sum_recursive(x, y))