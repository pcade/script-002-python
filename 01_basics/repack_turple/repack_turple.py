#!/bin/python3

def repack_turple(X, Z, Y, City):
    my_list = [X, Z , Y, City]
    del my_list[1]
    my_list[2], my_list[0] = my_list[0], my_list[2]
    my_list[1], my_list[2] = my_list[2], my_list[1]
    my_list[0] = my_list[0].lower()
    return(my_list)

print(repack_turple('0000000', '1111111', '22222222', 'dDDDDD'))

