#!/bin/python3

#digit = int(input("Введите число: "))
#if digit / 2 == 1:
#    print('Число '+ digit +' является простым')
#elif digit % 2 == 0:
#    print("Число '{digit}' не является простым")
#else:
#    print(f'Число {digit} является простым')



def prime(digit):
    if digit / 2 == 1 or digit / 3 == 1:
        print(f'Число {digit} является простым')
    elif digit % 2 == 0 or digit % 3 == 0:
        finder = digit + 1
        print(finder)
        while finder % 2 != 0 or finder % 3 != 0:
            finder += 1
            print(finder)
        print(f"Следующее простое число после {digit} это {finder}")
    else:
        print(f'Число {digit} является простым')

digit = int(input("Введите число: "))
prime(digit)