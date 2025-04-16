"""
На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
Известно, что вводимые числа по абсолютной величине не превышают 10^6.
Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности
и максимальное отрицательное число в последовательности.
Если отрицательных чисел нет, требуется вывести на экран «NO» (без кавычек).
Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их ровно 5).
Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

Примечание. При необходимости вы можете добавить необходимые строки кода.
"""

mx = -10000000  # Если условие брать по задаче, то выводится минимальное, а не максимальное число!
s = 0
for i in range(10):  # Неправильно был указан диапазон 11
    x = int(input())
    if x < 0:
        s += x  # Сумма отрицательных чисел должна увеличиваться, а не переопределяться
        if x > mx:  # Условие в программе выводило максимальное число во всей последовательности, перенес отступ
            mx = x
# Программа не выводила случай, когда отрицательных чисел нет
if s == 0:
    print('NO')
else:
    print(s)
    print(mx)
