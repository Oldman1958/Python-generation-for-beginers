"""
В саду 88n фруктовых деревьев, из них 32n яблони, 22n груши, 16n слив и 17n вишен.
В какой системе счисления посчитаны деревья?

Примечание. Переведите числа из n-ой системы счисления в десятичную и составьте уравнение.

88n = 32n + 22n + 16n + 17n
"""
for n in range(8, 16):
    if 8 * n + 8 == (3 * n + 2) + (2 * n + 2) + (n + 6) + (n + 7):
        print(n)
