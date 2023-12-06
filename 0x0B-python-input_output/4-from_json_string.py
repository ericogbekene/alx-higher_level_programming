#!/usr/bin/python3
""" return an object represented by Json """
import json


def from_json_string(my_str):
    """ to return a python object """

    data = json.loads(my_str)
    return data
