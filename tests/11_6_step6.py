"""
На вход программе подается строка текста, содержащая различные натуральные числа.
Вам необходимо переставить максимальный и минимальный элементы местами и вывести измененную строку.
"""
s = list(map(int, input().split()))
a = s.index(min(s))
b = s.index(max(s))
s[a], s[b] = s[b], s[a]
print(*s)
