#!/usr/bin/python3
""" divide the elements of a matrix """


def matrix_divided(matrix, div):
    """ function to divide a matrix

    Args:
        matrix: to be divided
        div: the divisor
    raise:
        TypeError:
        ValueError:

    """

    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    len_row = len(matrix[0])
    if not all(len(row) == len_row for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        matrix_two = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            element = (i / div)
            element = float("{:.2f}".format(element))
            matrix_two.append(element)
        new_matrix.append(matrix_two)
    return new_matrix
