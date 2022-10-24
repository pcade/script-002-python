#!/bin/python3

from unittest.result import failfast


final_list =[]
string = 'MyProgram V1.2.3 Copyright (c) 2022'
second_string = string.split(' ')
therd_string = second_string[1].split('.')
for char in therd_string[0]:
    therd_string.insert(0, char)
del therd_string[2]
therd_string[0], therd_string[1] = therd_string[1], therd_string[0]
zero = 'Версия:  '
first = therd_string[1]
second = therd_string[2]
therd = therd_string[3]
print(f"{zero}{first}.{second}.{therd}")