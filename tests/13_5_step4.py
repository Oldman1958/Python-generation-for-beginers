"""
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num
и возвращает первое простое число, большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

Примечание 2. Приведённый ниже код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
должен выводить:

7
11
17
"""


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
def get_next_prime(num):
    num += 1
    while is_prime(num) is False:
        num += 1

    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
