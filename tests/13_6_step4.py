"""
Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения:
длину окружности и площадь круга, ограниченного данной окружностью.
"""


# объявление функции
def get_circle(radius):
    from math import pi
    l_circle = 2 * pi * radius
    l_square = pi * radius ** 2
    return l_circle, l_square


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
