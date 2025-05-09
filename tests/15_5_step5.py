"""
Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря со сдвигом вправо на 10 символов.

Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).
"""
text = "Блажен, кто верует, тепло ему на свете!"
rot = 10
out_message = ''
alph_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in text:
    if i in alph_up:
        k = (alph_up.index(i) + rot) % 32
        out_message += alph_up[k]
    elif i in alph_low:
        k = (alph_low.index(i) + rot) % 32
        out_message += alph_low[k]
    else:
        out_message += i
print(out_message)

"""
Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп! - правильный ответ!
"""
