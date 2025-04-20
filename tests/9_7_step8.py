"""
На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий ему
код из таблицы символов Unicode.
"""
simbols = list(map(str, input()))
for i in range(len(simbols)):
    print(ord(simbols[i]), end=' ')


