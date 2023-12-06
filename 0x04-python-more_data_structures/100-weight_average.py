#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    n = 0
    for i in my_list:
        x += (i[0] * i[1])
        n += i[1]
    return x / n
