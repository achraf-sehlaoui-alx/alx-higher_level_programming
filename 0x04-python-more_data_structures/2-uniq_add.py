#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    new_list = my_list.copy()
    for i in new_list:
        n = new_list.count(i)
        if n > 1:
            for j in range(n - 1):
                new_list.remove(i)
    for i in new_list:
        s += i
    return s
