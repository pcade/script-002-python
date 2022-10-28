#!/bin/python3

def souvenirs(S: float, B: float) -> str:
    result = round(((S*75) + (B*112)), 2) # 75 and 112 constant
    return(f"Общий вес посылки равен {result}")

S = float(input("Введите количество сувениров: "))
B = float(input("Введите количество безделушек: "))
print(souvenirs(S, B))