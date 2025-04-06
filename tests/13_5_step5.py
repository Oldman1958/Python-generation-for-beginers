"""
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и
возвращает значение True, если пароль является надежным и False - в противном случае.

Пароль является надежным если:
его длина не менее 8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
"""


# объявление функции
def is_password_good(password):
    count_up = 0
    count_low = 0
    count_d = 0
    if len(password) < 8:
        return False
    for elem in password:
        if elem.isupper():
            count_up += 1

        if elem.islower():
            count_low += 1

        if elem.isdigit():
            count_d += 1

    return True if count_up >= 1 and count_low >=1 and count_d >= 1 else False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
