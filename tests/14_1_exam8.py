"""
Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en и number
– номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.
"""


# объявление функции
def get_month(language, number):
    lng_ru = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
              9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

    lng_en = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
              9: 'september', 10: 'october', 11: 'november', 12: 'december'}
    if language == 'ru':
        return lng_ru.get(number)
    elif language == 'en':
        return lng_en.get(number)


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
