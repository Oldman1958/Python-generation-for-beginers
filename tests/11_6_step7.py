"""
На вход программе подается строка, содержащая английский текст.
Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
"""
s = input().lower().split()
print(s.count('a') + s.count('an') + s.count('the'))
