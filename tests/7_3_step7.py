"""
На вход программе подаётся натуральное число n.
Напишите программу, которая вычисляет значение выражения (1+1/2+1/3+…+1/n)−ln(n).

Формат входных данных
На вход программе подаётся натуральное числоn.

Формат выходных данных
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.
"""

from math import log

n = int(input())
count = 1
for i in range(2, n + 1):
    count += 1 / i
print(count - log(n))
