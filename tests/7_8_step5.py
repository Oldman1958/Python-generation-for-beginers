"""
Дано натуральное число n(n≤ 9). Напишите программу, которая печатает таблицу размером n×3,
состоящую из данного числа (числа отделены одним пробелом).

Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу размером n×3, состоящую из данного числа.

Примечание. В конце строки может быть пробел.
"""

n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
