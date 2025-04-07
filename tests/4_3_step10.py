"""
На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:

карман 0 – зеленый;
для карманов с 1 по 10 карманы с нечётным номером имеют красный цвет, карманы с чётным номером – черный;
для карманов с 11 по 18 карманы с нечётным номером имеют черный цвет, карманы с чётным номером – красный;
для карманов с 19 по 28 карманы с нечётным номером имеют красный цвет, карманы с чётным номером – черный;
для карманов с 29 по 36 карманы с нечётным номером имеют черный цвет, карманы с чётным номером – красный.
Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным.
Программа должна вывести сообщение об ошибке, если пользователь вводит число,
которое лежит вне диапазона от 0 до 36.

Формат входных данных
На вход программе подаётся одно целое число.

Формат выходных данных
Программа должна вывести цвет кармана либо сообщение «ошибка ввода» (без кавычек),
если введённое число лежит вне диапазона от 0 до 36.
"""

n = int(input())
chet = 0
if n > 36 or n < 0:
    print('ошибка ввода')
else:
    if n % 2 == 0:
        chet = 1
    if 1 <= n <= 10 or 19 <= n <= 28:
        print('черный' if chet else 'красный')
    elif 11 <= n <= 18 or 29 <= n <= 36:
        print('красный' if chet else 'черный')
    else:
        print('зеленый')
