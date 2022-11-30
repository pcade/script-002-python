#!/bin/python3


def currency(EUR_RUB: float, RUB: float) -> str:
    CURRENCY = RUB//EUR_RUB
    return(f"По курсу {EUR_RUB} рублей за 1 евро, на {RUB} рублей вы купите {CURRENCY} евро.")

EUR_RUB = float(input("Введите курс EUR/RUB: "))
RUB = float(input("Введите количество рублей: "))

print(currency(EUR_RUB, RUB))