"""
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
"""


def print_digit_sum(n):
    count = 0
    for i in n:
        count += int(i)
    print(count)


print_digit_sum(input())
