"""
Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нём;
сколько раз в нём встречается последняя цифра;
количество чётных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести её);
сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).
Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке, каждую на отдельной строке.
"""

n = int(input())
last_digit = 0
first_c_l = n % 10
digit_3 = 0
count_last = 0
digit_chet = 0
sum_m5 = 0
mult_7 = 1
count_0_5 = 0
while n != 0:
    last_digit = n % 10
    if last_digit == 3:
        digit_3 += 1
    if last_digit == first_c_l:
        count_last += 1
    if last_digit % 2 == 0:
        digit_chet += 1
    if last_digit > 5:
        sum_m5 += last_digit
    if last_digit > 7:
        mult_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        count_0_5 += 1
    n //= 10
print(digit_3)
print(count_last)
print(digit_chet)
print(sum_m5)
print(mult_7)
print(count_0_5)
