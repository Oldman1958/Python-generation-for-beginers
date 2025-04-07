"""
Напишите программу, которая классифицирует треугольник на основе длин его сторон.
Программа должна принимать три числа, каждое из которых представляет собой длину одной из его сторон.
В результате программа должна определить, является ли треугольник равносторонним, равнобедренным или разносторонним.

Формат входных данных
На вход программе подаются три числа (каждое на отдельной строке) – длины сторон существующего треугольника.

Формат выходных данных
Программа должна вывести на экран текст – тип треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).
"""

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a != b and a != c and b != c:
    print('Разносторонний')
else:
    print('Равнобедренный')
