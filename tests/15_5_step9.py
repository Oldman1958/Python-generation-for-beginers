"""
Текст "Hawnj pk swhg xabkna ukq nqj." был получен в результате шифрования алгоритмом Цезаря с сдвигом вправо на n
символов. Расшифруйте данный текст.

Примечание. Считайте, что n∈[0;25].
"""
text = "Hawnj pk swhg xabkna ukq nqj."
# rot = 25
out_message = ''
alph_low = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alph_up = alph_low.upper()
rot = 0
while rot <= 25:
    for i in text:
        if i in alph_up:
            k = (alph_up.index(i) - rot) % 26
            out_message += alph_up[k]
        elif i in alph_low:
            k = (alph_low.index(i) - rot) % 26
            out_message += alph_low[k]
        else:
            out_message += i
    print(out_message)
    rot += 1
    out_message = ''
