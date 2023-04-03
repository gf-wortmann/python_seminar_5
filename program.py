# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
#  A = 3; B = 5 -> 243 (3⁵)
#  A = 2; B = 3 -> 8

x, y = input('enter 2 numbers: ').split()
x = int(x)
y = int(y)


def power_recursive(a, b, c=1):
    if b == 1:
        return a
    else:
        if c == 1:
            c = a
        a *= c
        return power_recursive(a, b - 1, c)


print(power_recursive(x, y))