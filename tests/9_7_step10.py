"""
Модератору Сэму за каждый символ его сообщений в комментариях Тимур платит в 🐝 (пчёлках-coin) по следующему тарифу:

<код символа в таблице Unicode>×3 🐝

А стоимость всего сообщения складывается из суммы стоимостей всех символов.
Сэму захотелось подсчитать, сколько 🐝 он зарабатывает за свои ответы в комментариях, и просит вас помочь ему.

На вход программе подаётся строка текста.
Требуется написать программу, которая находит стоимость сообщения Сэма в 🐝 и выводит текст в следующем формате:

Текст сообщения: '<текст сообщения Сэма>'
Стоимость сообщения: <стоимость сообщения Сэма>🐝
Формат входных данных
На вход программе подаётся строка текста – очередной ответ Сэма в комментариях.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. 🐝 (пчёлка-coin) – виртуальная валюта команды BEEGEEK, которой Тимур расплачивается со своими сотрудниками.
"""

com_in = input()
cash = 0
for i in range(len(com_in)):
    cash += ord(com_in[i]) * 3

print(f"Текст сообщения: '{com_in}'")
print(f"Стоимость сообщения: {cash}🐝")
