"""
Дано натуральное число n(n≤9).
Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n (включительно) в соответствии с примером.

Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу сложения для всех чисел от 1 до n.

Примечание 1. Таблицу сложения подразумеваем от 1 до 9 (включительно).

Примечание 2. В конце строки может быть пробел.
"""

n = int(input())
summ = 0
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()
