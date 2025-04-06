"""
На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
k-ую букву из введенных строк на одной строке без пробелов.
"""
n = int(input())
s = []
for i in range(n):
    s.append(input())
k = int(input())
out = []
for i in range(n):
    if len(s[i]) < k:
        continue
    else:
        out.append(s[i][k - 1])
print(*out, sep='')
