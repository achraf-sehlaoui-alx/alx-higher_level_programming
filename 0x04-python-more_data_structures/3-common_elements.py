#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_c = []
    for i in set_1:
        for j in set_2:
            if i == j:
                list_c.append(i)
    return list_c
