"""
На числовой прямой даны два отрезка: [a1;b1] и [a2;b2]. Напишите программу, которая находит их пересечение.

Пересечением двух отрезков может быть:

отрезок:

точка:

пустое множество:

Формат входных данных
На вход программе подаются четыре целых числа a1, b1, a2, b2, каждое на отдельной строке.
Гарантируется, что a1<b1, и a2<b2.
Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку,
либо текст «пустое множество» (без кавычек).
"""

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if ((a1 < a2 and b1 < b2) or (a2 < a1 and b2 < b1)) and b1 < a2:
    print('пустое множество')
elif a2 < a1 and b2 < a1:
    print('пустое множество')
elif (a1 < a2 and b1 > b2) or (b1 == b2 and a1 < a2) or (a1 == a2 and b2 < b1):
    print(a2, b2)
elif a1 < a2 and (a2 < b1 < b2):
    print(a2, b1)
elif a2 < a1 and (a1 < b2 < b1):
    print(a1, b2)
elif (a2 < a1 and b2 > b1) or (a1 == a2 and b1 == b2) or (a1 == a2 and b1 < b2) or (b1 == b2 and a2 < a1):
    print(a1, b1)
elif a2 == b1:
    print(a2)
elif b2 == a1:
    print(a1)
