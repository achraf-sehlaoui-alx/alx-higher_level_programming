#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        tmp = i.copy()
        j = list(map(lambda x: x * x, tmp))
        new_matrix.append(j)
    return new_matrix
