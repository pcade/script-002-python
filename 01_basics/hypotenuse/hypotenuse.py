#!/bin/python3

import math

def hypotenuse(line_1: float, line_2: float) -> str:
    result = round((math.sqrt(line_1) + math.sqrt(line_2)),2)
    return(f"Длина гипотенузы {result}")    

line_1 = float(input("Введите длину первого катета: "))
line_2 = float(input("Введите длину второго катета: "))

print(hypotenuse(line_1, line_2))