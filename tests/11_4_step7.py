"""
На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
затем k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются
одновременно все поисковые запросы.

Формат входных данных
На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве,
затем число k, затем сами поисковые запросы.

Формат выходных данных
Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.

Примечание. Поиск не должен быть чувствителен к регистру символов.
"""
n = int(input())
s = []
for i in range(n):
    s.append(input())
k = int(input())
r = []
for i in range(k):
    r.append(input())
out = []
for h in range(n):
    count = 0
    for g in range(k):
        if r[g].lower() in s[h].lower():
            count += 1
    if count == len(r):
        out.append(s[h])
print(*out, sep='\n')
