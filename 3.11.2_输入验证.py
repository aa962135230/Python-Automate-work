# -*- coding:utf-8 -*-


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


print('Enter number:')
try:
    yournum = int(input())

    cnum = collatz(yournum)
    while cnum != 1:
        print(cnum)
        cnum = collatz(cnum)
    print(cnum)


except:
    print('错误：请输入整数')
