#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = 0
    a1 = 0
    b0 = 0
    b1 = 0
    za = len(tuple_a)
    zb = len(tuple_b)
    if za == 1:
        a0 = tuple_a[0]
    elif za >= 2:
        a0, a1 = tuple_a
    if zb ==1:
        b0 = tuple_b[0]
    elif zb >= 2:
        b0, b1 = tuple_b
    a = a0 + b0
    b = a1 + b1
    tuple_c = (a, b)
    return tuple_c
