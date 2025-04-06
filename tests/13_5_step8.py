"""
BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password
и возвращает значение True, если пароль является действительным паролем BEEGEEK банка и False - в противном случае.
"""


# объявление функции
def is_prime(num):
    count = 0
    if num == 0 or num == 1:
        return False
    else:
        for i in range(1, num):
            if num % i == 0:
                count += 1
    return False if count > 1 else True


# объявление функции
def is_valid_password(password):
    count = 0
    if len(password) != 3:
        return False
    else:
        if int(password[2]) % 2 == 0:
            count += 1
        if password[0] == password[0][::-1]:
            count += 1
        if is_prime(int(password[1])):
            count += 1
    return True if count == 3 else False


# считываем данные
psw = input().split(':')

# вызываем функцию
print(is_valid_password(psw))
