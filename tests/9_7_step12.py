"""
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря.
Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного
мира, поэтому ученые из НКР не могут понять, как именно нужно декодировать данные сообщения. Напишите программу для
декодирования этого шифра.

Формат входных данных
В первой строке дается число n (1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со
строчными латинскими буквами.

Формат выходных данных
Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно декодировать сообщение,
а не закодировать.
"""
n = int(input())
in_message = input()
out_message = ''
for i in range(len(in_message)):
    a = ord(in_message[i]) - n
    if a < 97:
        a += 26
    out_message += chr(a)
print(out_message)
