"""
На вход программе подается четное число n, n≥2.
Напишите программу, которая выводит список четных чисел  [2, 4, 6, ..., n].
"""
n = int(input())
print([i for i in range(2, n + 1, 2)])
