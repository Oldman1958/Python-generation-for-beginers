"""
Зашифруйте текст "To be, or not to be, that is the question!" алгоритмом Цезаря с сдвигом вправо на 17 символов.
"""
text = "To be, or not to be, that is the question!"
rot = 17
out_message = ''
alph_low = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alph_up = alph_low.upper()
for i in text:
    if i in alph_up:
        k = (alph_up.index(i) + rot) % 26
        out_message += alph_up[k]
    elif i in alph_low:
        k = (alph_low.index(i) + rot) % 26
        out_message += alph_low[k]
    else:
        out_message += i
print(out_message)
