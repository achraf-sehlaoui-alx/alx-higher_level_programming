#!/usr/bin/python3
def element_at(my_list, idx):
    z = len(my_list)
    if idx < 0:
        return None
    elif idx >= z:
        return None
    else:
        return my_list[idx]
