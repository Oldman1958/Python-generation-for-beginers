"""
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка,
состоящих из целых чисел, и объединяет их в один отсортированный список.

Примечание 1. Списки list1 и list2 могут иметь разную длину.

Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него.
"""


# объявление функции
def merge(list1, list2):
    return sorted(list1 + list2)


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
