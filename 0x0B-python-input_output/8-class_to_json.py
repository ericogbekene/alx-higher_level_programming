#!/usr/bin/python3
""" script to return a dict representation from an object """


def class_to_json(obj):
    """
    returns a ditionary

    """
    return obj.__dict__
