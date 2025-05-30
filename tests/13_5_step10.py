"""
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и
преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
должен выводить:

this_is_camel_cased
is_prime_number
"""


# объявление функции
def convert_to_python_case(text):
    out = ''
    for i in range(len(text)):
        if text[i].isupper() and i != 0:
            out += '_' + text[i]
        else:
            out += text[i]
    return out.lower()


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
