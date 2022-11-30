#!/bin/python3

def odd_even(finder: int) -> str:
    if finder % 2 != 0 :
        finder = ("Введённое число - не чётное")
    else:
        finder = ("Введённое число - чётное")
    return(finder)

finder = int(input("Введите целое число: "))
print(odd_even(finder))