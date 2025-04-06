"""
Используя метод format(), дополните приведенный код так, чтобы он вывел текст:

In 2010, someone paid 10K Bitcoin for two pizzas.

s = 'In {0}, someone paid {1} {2} for two pizzas.'

print()

От предыдущей отличается буквой К!!!
"""
year = 2010
pay = '10K'
val = 'Bitcoin'

s = f'In {year}, someone paid {pay} {val} for two pizzas.'

print(s)