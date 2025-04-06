"""
Числовая угадайка
Не полный вариант

import random


def is_valid(text):
    return text.isdecimal() and 1 <= int(text) <= 100


n = random.randint(0, 100)
print('Добро пожаловать в числовую угадайку')
count_user = 0
while True:
    guess = input("Введите целое число от 1 до 100: ")
    count_user += 1
    if is_valid(guess):
        guess = int(guess)
        if guess < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif guess > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif guess == n:
            print("Вы угадали, поздравляем!")
            print("Общее число попыток", count_user)
            break
        else:
            print("Спасибо, что играли в числовую угадайку. Еще увидимся")
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
"""

# Полный вариант

import random as ra


def is_invalid_input(num):
    if not num.isdigit():
        print('Неверный ввод! Нужно ввести целое число больше 1')
        return False, 0
    if int(num) not in range(1, int(num) + 1):
        print(f'Неверный ввод! Нужно ввести целое число от 1 до {num}')
        return False, 0
    return True, int(num)


def guess_number(n):
    cnt = 0
    while True:
        num_str = input()
        correct, num = is_invalid_input(num_str)
        if not correct:
            break
        elif num < n:
            print('Слишком мало, попробуйте еще раз')
            cnt += 1
            continue
        elif num > n:
            print('Слишком много, попробуйте еще раз')
            cnt += 1
            continue
        else:
            print(f'Вы угадали c {cnt} попытки, поздравляем!')
            break


input_choice = 'д'
while input_choice == 'д':
    print('Введите правую границу диапазона')
    r_border = input()
    correct, r_border = is_invalid_input(r_border)
    if not correct:
        continue
    n = ra.randrange(1, r_border)
    print(f'Загадано число от 1 до {r_border}. Попробуйте угадать это число ')
    guess_number(n)
    print('Хотите поиграть еще? Если да, на нажмите д\nЕсли нет, то нажмите н')
    input_choice = input()
    if input_choice != 'н':
        print('Вы так и не сделали свой выбор!')
    print('Тогда до встречи! Всего вам доброго!')
