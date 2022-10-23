#!/bin/python3



import math

def hypotenuse_fun(line_1, line_2):
    hypotenuse = line_1 + line_2
    print("Длина гипотенузы " "%.2f" %hypotenuse)

line_1 = math.sqrt(float(input("Введите длину первого катета: ")))
line_2 = math.sqrt(float(input("Введите длину второго катета: ")))

hypotenuse_fun(line_1, line_2)