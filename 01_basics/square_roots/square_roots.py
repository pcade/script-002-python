#!/bin/python3

from math import sqrt

def first(a: float, b: float, c: float) -> str:
    D = b*b - 4*a*c
    if D == 0:
        x = (-b + sqrt(D)) / (2 * a) 
        return(f'x = {x}')
    elif D > 0:
        x1 = round((-b + sqrt(D)) / (2 * a), 1)
        x2 = round((-b - sqrt(D)) / (2 * a), 1)
        return(f'x1 = {x1}\nx2 = {x2}')
    else:
        return('Корней нет') 

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

print(first(a, b, c))  

