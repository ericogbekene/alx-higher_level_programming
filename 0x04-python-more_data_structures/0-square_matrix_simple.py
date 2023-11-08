#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rown in matrix:
        new_row = []
        for i in rown:
            new_row.append(i * i)
        new_matrix.append(new_row)
    return new_matrix
