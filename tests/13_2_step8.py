"""
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.
"""
s = input()
n = int(input())


def draw_triangle(fill, base):
    middle = (base // 2) + 1
    for i in range(middle + 1):
        print(fill * i)
    for j in range(middle - 1, 0, -1):
        print(fill * j)


draw_triangle(s, n)
print()
