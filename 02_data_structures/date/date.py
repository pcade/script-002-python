#!/bin/python3

def date_() -> str:
    first_date = 0
    first_date = input('Введите дату через тере: ')
    if '-' not in first_date:
        print('\nне корректные данные\n')
        date_()
    if 3 != len(first_date.split('-')):
        print('\nне корректные колличество - данные\n')
        date_()   
    if '-' in first_date:
        second_date = first_date.split('-')
        therd_second_date = second_date[2]
        second_date.remove(second_date[2])
        second_date.insert(0, therd_second_date)
        print(f"Преобразованная дата: {second_date[0]}.{second_date[1]}.{second_date[2]}") 
        exit()
    
date_()
