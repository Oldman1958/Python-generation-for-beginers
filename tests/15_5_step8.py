"""
Текст "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd." был получен в результате шифрования алгоритмом
Цезаря со сдвигом вправо на 25 символов. Расшифруйте данный текст.
"""
text = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
rot = 25
out_message = ''
alph_low = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alph_up = alph_low.upper()
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
