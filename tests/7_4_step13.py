"""
На вход программе подаётся последовательность целых чисел от 1 до 5, характеризующее оценку ученика,
каждое число на отдельной строке.
Концом последовательности является любое неположительное число либо число, большее 5.
Напишите программу, которая выводит количество пятерок.

Формат входных данных
На вход программе подаётся последовательность чисел, каждое число на отдельной строке.

Формат выходных данных
Программа должна вывести количество пятерок.

Примечание. Не забываем, что неположительными числами являются все отрицательные числа и число 0.
"""

count = 0
n = int(input())
while 0 < n <= 5:
    if n == 5:
        count += 1
    n = int(input())
print(count)
