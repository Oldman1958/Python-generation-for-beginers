"""
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных
На вход программе подаётся одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке, каждое на отдельной строке.
"""

n = int(input())
sum_digit = 0
count_digit = 0
mlpl_digit = 1
end_digit = 0
begin_digit = 0

mdl_summ_digit = 0
while n != 0:
    last_digit = n % 10
    if count_digit == 0:
        end_digit = last_digit
    sum_digit += last_digit
    count_digit += 1
    mlpl_digit *= last_digit
    begin_digit = last_digit
    n //= 10

print(sum_digit)
print(count_digit)
print(mlpl_digit)
print(sum_digit / count_digit)
print(begin_digit)
print(begin_digit + end_digit)
