#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    za = len(tuple_a)
    zb = len(tuple_b)
    a0 = tuple_a[0] if za >= 1 else 0
    a1 = tuple_a[1] if za >= 2 else 0
    b0 = tuple_b[0] if zb >= 1 else 0
    b1 = tuple_b[1] if zb >= 2 else 0
    a = a0 + b0
    b = a1 + b1
    tuple_c = (a, b)
    return tuple_c
