"""
Текст "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг." был получен в результате шифрования алгоритмом Цезаря сj сдвигом вправо на
7 символов. Расшифруйте данный текст.

Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).
"""
text = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
rot = 7
out_message = ''
alph_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in text:
    if i in alph_up:
        k = (alph_up.index(i) - rot) % 32
        out_message += alph_up[k]
    elif i in alph_low:
        k = (alph_low.index(i) - rot) % 32
        out_message += alph_low[k]
    else:
        out_message += i
print(out_message)
