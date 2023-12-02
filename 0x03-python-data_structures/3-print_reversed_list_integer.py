#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    z = len(my_list)
    if not my_list:
        return None
    for i in range(z - 1, -1, -1):
        print("{:d}".format(my_list[i]))
