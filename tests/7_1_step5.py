"""
На вход программе подаётся натуральное число n(n∈[1;20]).

Напишите программу, которая печатает звёздный прямоугольник размерами n×19.

Формат входных данных
На вход программе подаётся натуральное число n(n∈[1;20]) – высота звёздного прямоугольника.

Формат выходных данных
Программа должна вывести звёздный прямоугольник размерами n×19.

Примечание. Для печати звёздной линии используйте умножение строки на число.
"""

n = int(input())
for i in range(n):
    print('*' * 19)
