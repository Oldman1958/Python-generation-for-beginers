"""
На вход программе подается натуральное число в десятичной системе счисления. Напишите программу, которая переводит его в
двоичную, восьмеричную и шестнадцатеричную системы счисления.
"""
n = int(input())
print(bin(n)[2:])
print(oct(n)[2:])
print(hex(n)[2:].upper())
