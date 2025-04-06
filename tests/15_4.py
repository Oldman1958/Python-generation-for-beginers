"""
Генератор безопасных паролей

Подключите модуль random;
Создайте строковые константы:
digits: 0123456789;
lowercase_letters: abcdefghijklmnopqrstuvwxyz;
uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
punctuation: !#$%&*+-=?@^_.
Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.

Программа должна запрашивать у пользователя следующую информацию:

Количество паролей для генерации;
Длину одного пароля;
Включать ли цифры 0123456789?
Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
Включать ли символы !#$%&*+-=?@^_?
Исключать ли неоднозначные символы il1Lo0O?

САМ!!! Полностью сам!!!
"""
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

psw_count = int(input("Введите количество паролей для генерации: "))
psw_len = int(input("Введите  длину одного пароля: "))
psw_digit = input("Включать в пароль цифры?: ")
if psw_digit.lower() == 'да':
    chars += digits
psw_up = input("Включать в пароль заглавные буквы?: ")
if psw_up == 'да':
    chars += uppercase_letters
psw_low = input("Включать в пароль строчные буквы?: ")
if psw_low == 'да':
    chars += lowercase_letters
psw_sim = input("Включать в пароль специальные символы?: ")
if psw_sim == 'да':
    chars += punctuation
psw_same = input("Исключать из пароля неоднозначные символы?: ")
if psw_same == 'да':
    for i in chars:
        if i == 'i' or i == 'l' or i == '1' or i == 'L' or i == "o" or i == 'O' or i == '0':
            chars.replace(i, '')


def generate_password(length, chrs):
    psw = ''
    for i in range(length):
        psw += random.choice(chrs)
    return psw


for i in range(psw_count):
    print(generate_password(psw_len, chars))
