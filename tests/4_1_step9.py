"""
Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
последовательными членами арифметической прогрессии.

Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести «YES» (без кавычек) или «NO» (без кавычек) в соответствии с условием задачи.
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())
print('YES' if n2 - n1 == n3 - n2 else 'NO')