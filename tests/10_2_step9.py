"""
На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
s = input()
for i in s:
    if i == '@':
        continue
    else:
        print(i, sep='', end='')
