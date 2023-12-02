#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        z = len(i)
        if i == 0:
            print()
        for j in range(z):
            print("{:d}".format(i[j]), end="\n" if j == z - 1 else " ")
