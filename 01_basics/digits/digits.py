#!/bin/python3


def digit(any: str) -> int:
    finder = 0
    my_list = [int(i) for i in any]
    for element in range(0, len(my_list)):
        finder = finder + my_list[element]
    return(f"Сумма цифр равна {finder}")

any = input("Введите число: ")

print(digit(any))