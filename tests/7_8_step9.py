"""
Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:

1
22
333
4444
55555
...

Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.

Примечание. Используйте вложенный цикл for.
"""

n = int(input())
for i in range(n + 1):
    for j in range(i):
        print(i, end='')
    print()
