#!/bin/python3

digit = int(input('Введите количество баллов: '))
my_struct = {digit in range(0, 54) : '2', digit in range(55, 69) : '3', digit in range(70, 84) : '4', digit in range(85, 100) : '5'}
print(f'\n| Баллы  | Оценка |\n| ------ | ------ |\n|   {digit}   |   {my_struct[True]}    |\n')