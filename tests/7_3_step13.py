"""
На вход программе подаются натуральное число n(n≥2), а затем n различных натуральных чисел последовательности,
каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

Формат входных данных
На вход программе подаются натуральное число n(n≥2), а затем n различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два наибольших числа последовательности, каждое на отдельной строке.
"""

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
first = 0
second = 0
for i in s:
    if i > first:
        second = first
        first = i
    elif i < first and i > second:
        second = i

print(first)
print(second)
