"""
Даны две различные клетки шахматной доски.
Напишите программу, которая определяет, может ли король попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести «YES» (без кавычек), если из первой клетки ходом короля можно попасть во вторую,
или «NO» (без кавычек) в противном случае.

Формат входных данных
На вход программе подаются четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
"""

n = int(input())
m = int(input())
i = int(input())
j = int(input())
print('YES' if abs(n - i) <= 1 and abs(m - j) <= 1 else 'NO')
