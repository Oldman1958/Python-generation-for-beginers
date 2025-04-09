"""
На вход программе подаются три натуральных числа m,p,n:

m: стартовое количество организмов;
p: среднесуточное увеличение в %;
n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции организмов с 1-го по n-й день (включительно).
Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.

Формат входных данных
На вход программе подаются три натуральных числа (каждое на отдельной строке): m,p,n.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Задача решается через сложный процент.
"""

m = float(input())
p = int(input())
n = int(input())
for i in range(n):
    print(i + 1, m)
    m *= (1 + p / 100)
