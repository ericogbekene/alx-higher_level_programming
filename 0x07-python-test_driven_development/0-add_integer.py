#!/usr/bin/python3
""" function to add two integers """


def add_integer(a, b=98):
    """ my addition function
    Usage:
        >>> add_integer(4, 7)
        11
        >>> add_integer(7, -1)
        6
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    if a == None:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    return (a + b)
