#!/usr/bin/python3
def no_c(my_string):
    z = len(my_string)
    new_str = ""
    for i in range(z):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str += my_string[i]
    return new_str
