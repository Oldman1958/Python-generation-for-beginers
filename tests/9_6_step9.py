"""
Вследствие кибератаки на банк "Разбогатеем вместе" сломался алгоритм, выводящий курсы валют для определенной даты в
мобильном приложении. Технический отдел банка просит вас исправить ситуацию и наладить вывод. На вход программе подаются
следующие значения:

дата (в формате ДД-ММ-ГГГГ)
курс доллара (сколько российских рублей стоит 1 доллар)
курс юаня (сколько российских рублей стоит 1 юань)
Напишите программу, которая выводит строку, показывающую, сколько российских рублей стоит 1 доллар и 1 юань на указанную
дату в формате:

На <дата>: 1$ = <курс доллара>₽, 1¥ = <курс юаня>₽
Формат входных данных
На вход программе подается 3 строки: дата, курс доллара и курс юаня.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
date = input()
taller_rate = input()
yuan_rate = input()
print(f'На {date}: 1$ = {taller_rate}₽, 1¥ = {yuan_rate}₽')
