"""
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу,
которая выводит инициалы человека.
"""
fio = input().split()
print(fio[0][0], fio[1][0], fio[2][0], sep='.', end='.')
