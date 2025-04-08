"""
В математике выделяют следующие средние значения:

среднее арифметическое чисел a и b: (a+b) / 2;

среднее геометрическое чисел a и b: (a*b) ^ 1/2;

среднее гармоническое чисел  (2ab) / a + b;

среднее квадратичное чисел a и b: ((a^2 + b^2) / 2) ^ 1/2.
Формат входных данных
На вход программе подаются два положительных действительных числа a и b, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести 4 числа (каждое на отдельной строке)
– среднее арифметическое, геометрическое, гармоническое и квадратичное.
"""

from math import sqrt

a = float(input())
b = float(input())
print((a + b) / 2)
print(sqrt(a * b))
print((2 * a * b) / (a + b))
print(sqrt((a ** 2 + b ** 2) / 2))
