"""
Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

Формат входных данных
На вход программе подаётся положительное действительное число.

Формат выходных данных
Программа должна вывести цифру в соответствии с условием задачи.
"""

n = float(input())
first_digit = str(n % 1)
print(first_digit[2])
