#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    z = len(my_list)
    new_list = []
    for i in my_list:
        new_list.append(i)
    if idx < 0 or idx >= z:
        return new_list
    else:
        new_list[idx] = element
        return new_list
