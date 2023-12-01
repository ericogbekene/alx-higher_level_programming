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
    for row in matrix:
        matrix_two = []

        #if len(row[0]) != len(row[1]):
            #raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            #if not isinstance(i, (int, float)):
                #raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            element = (i / div)
            element = float("{:.2f}".format(element))
            matrix_two.append(element)
        new_matrix.append(matrix_two)
    return new_matrix
