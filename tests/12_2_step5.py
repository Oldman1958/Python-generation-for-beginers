"""
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая находит длину
самого длинного слова.

n = [i for i in input().split(' ')]
s = [len(elem) for elem in n]
"""
print(max([len(elem) for elem in [i for i in input().split(' ')]]))
