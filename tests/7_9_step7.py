"""
На вход программе подается два натуральных числа a и b (a<b). Напишите программу, которая находит все простые числа от
a до b включительно.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести все простые числа от a до b включительно, каждое на отдельной строке.

Примечание 1. Простое число – это натуральное число, единственными делителями которого являются только оно само и 1.

Примечание 2. Число 1 простым не является.
"""

def simple(n):
    if n <= 1:
        return False
    for el in range(2, int(n ** 0.5) + 1):
        if n % el == 0:
            return False
    return True


a = int(input())
b = int(input())
for i in range(a, b + 1):
    if simple(i):
        print(i)
