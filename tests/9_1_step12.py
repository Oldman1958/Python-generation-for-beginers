"""
На вход программе подаётся одна строка.
Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *,
и выводит текст в следующем формате:

Символ + встречается <n> раз
Символ * встречается <m> раз
где <n>, <m> – количество вхождений символов + и * в строку соответственно.

Формат входных данных
На вход программе подаётся одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""

s = input()
plus = 0
zv = 0
for i in s:
    if i == '+':
        plus += 1
    elif i == '*':
        zv += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', zv, 'раз')
