#!/bin/python3






def format(name: str, bonus: int, boost: float) -> str:
    first_string = "получил премию"
    second_string = "рублей или"
    final_string = "%."
    print(f"{name} получил премию {bonus} рублей или {boost*100} %.")
    print(name, first_string, bonus, second_string, (boost*100),final_string)
name = 'ВАСЯ'
bonus = 12345
boost = 0.12

format(name, bonus, boost)