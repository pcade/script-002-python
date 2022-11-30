#!/bin/python3


def grade(digit: int) -> str:
    my_struct = {digit in range(0, 54) : '2', digit in range(55, 69) : '3', digit in range(70, 84) : '4', digit in range(85, 100) : '5'}
    print(digit)
    if digit < 10:
        result = (f'\n| Баллы | Оценка|\n| ------| ------|\n|   {digit}   |   {my_struct[True]}   |\n')
    else:
        result = (f'\n| Баллы  | Оценка |\n| ------ | ------ |\n|   {digit}   |   {my_struct[True]}    |\n')
    return(result)

digit = int(input('Введите количество баллов: '))
print(grade(digit))