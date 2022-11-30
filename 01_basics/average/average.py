#!/bin/python3

import math

def average():
    my_list = []
    first_finder = input("Введите первое число: ")
    while True:
        next_finder = input("Введите следующее число: ")
        my_list.append(next_finder)
        if next_finder == "":
            break
    del my_list[-1]
    my_list.append(first_finder)
    return(round(sum(int(x) for x in my_list) / len(my_list),2))

print(average())