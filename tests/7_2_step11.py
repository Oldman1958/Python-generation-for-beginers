"""
Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n (от 1 до 10 включительно).

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести таблицу умножения на введённое число.

Примечание. В качестве знака умножения используйте английскую букву x.
"""

n = int(input())
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)
