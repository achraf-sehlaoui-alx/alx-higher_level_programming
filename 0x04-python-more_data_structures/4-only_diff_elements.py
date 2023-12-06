#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_d = list(set_1) + list(set_2)
    for i in set_1:
        for j in set_2:
            if i == j:
                n = list_d.count(i)
                for k in range(n):
                    list_d.remove(i)
    return list_d
