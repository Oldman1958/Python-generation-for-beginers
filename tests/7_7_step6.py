"""
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную цифру числа,
кратную 3. Если в числе нет цифр, кратных 3, требуется на экран вывести «NO» (без кавычек).
Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их ровно 5).
Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

Примечание 1. Число 0 делится на любое натуральное число.

Примечание 2. При необходимости вы можете добавить нужные строки кода.
"""

n = int(input())
# Неправильная инициализация переменной. Вначале она равна -1.
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        # Если последняя цифра больше максимальной
        if digit > max_digit:
            # Переопределяем именно максимальную цифру
            max_digit = digit
    # Неправильно отбрасывается последняя цифра
    n = n // 10
if max_digit != -1:
    print(max_digit)

else:
    print('NO')
