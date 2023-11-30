#!/usr/bin/python3
""" a function to print a square """


def print_square(size):
    """ function to print square

    Args:
        size - length of square
    raises:
        TypeError: if ssize is not int
        ValueError: if size is < 0

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
