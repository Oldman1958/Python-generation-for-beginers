"""
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты
квадратного уравнения ax^2+bx+c=0 и возвращает его корни в порядке возрастания.
"""


# объявление функции
def solve(a, b, c):
    from math import sqrt
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = x2 = -b / (2 * a)
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
    if x1 <= x2:
        return x1, x2
    else:
        return x2, x1


# считываем данные
ka, kb, kc = int(input()), int(input()), int(input())

# вызываем функцию
rx1, rx2 = solve(ka, kb, kc)
print(rx1, rx2)
