"""
На вход программе подаётся натуральное число n.
Напишите программу, которая выводит числа от 1 до n включительно за исключением:

чисел от 5 до 9 включительно;
чисел от 17 до 37 включительно;
чисел от 78 до 87 включительно.

Формат входных данных
На вход программе подаётся одно натуральное число n.

Формат выходных данных
Программа должна вывести числа в соответствии с условием задачи, каждое на отдельной строке.

Примечание. Используйте оператор continue.
"""

n = int(input())
for i in range(1, n + 1):
    if i < 5 or 9 < i < 17 or 37 < i < 78 or i > 87:
        print(i)
    else:
        continue
