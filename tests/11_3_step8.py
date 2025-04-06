"""
Напишите программу, выводящую следующий список:
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

Формат выходных данных
Программа должна вывести указанный список.

Примечание 1. Последний элемент списка должен состоять из 26 символов z.

Примечание 2. Английский алфавит (для копирования):
abcdefghijklmnopqrstuvwxyz
"""
alph = 'abcdefghijklmnopqrstuvwxyz'
s = []
for i in range(len(alph)):
    s.append(alph[i] * (i + 1))
print(s)
