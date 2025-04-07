"""
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

Примечание. Учитывайте, что числа могут быть равны.
"""

a = int(input())
b = int(input())
c = int(input())
s = a + b + c
print(max(a, b, c))
print(s - max(a, b, c) - min(a, b, c))
print(min(a, b, c))

