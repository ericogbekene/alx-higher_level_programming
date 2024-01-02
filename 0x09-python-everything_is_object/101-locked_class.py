#!/usr/bin/python3
""" locked class module """


class LockedClass:
    """
    a class that only allows dynamically creating instance attributes with a specific name
    """
    __slots__ = ["first_name"]
