"""
Дано натуральное число. Напишите программу, которая определяет,
является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» (без кавычек),
если последовательность его цифр при просмотре справа налево является упорядоченной по неубыванию,
или «NO» (без кавычек) в противном случае.
"""

n = int(input())
last_digit = 0
max_digit = 0
flag = True
while n > 0:
    last_digit = n % 10
    if last_digit < max_digit:
        flag = False
        break
    else:
        max_digit = last_digit
        n //= 10
print('YES' if flag else 'NO')
