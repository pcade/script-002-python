#!/bin/python3

result = float
my_list = []

while True:
    param = float(input("Ведите число : "))
    my_list.append(param)
    stop = input("Вы желаете продолжить ввод чисел - Yes or No ? ")
    if stop == 'N' or stop == 'n' or stop == 'NO' or stop == 'no' or stop == 'No' or stop == 'nO':
        break

if len(my_list) % 2 == 0:
    sorted_list = sorted(my_list, key= lambda x:float(x))
    position = int(len(my_list) / 2)
    result = (sorted_list[position] + sorted_list[position + 1]) / 2
    print(result)
else:
    sorted_list = sorted(my_list, key= lambda x:float(x))
    position = int(float(len(my_list) / 2 + 0.5))
    result = sorted_list[position]
    print(result)