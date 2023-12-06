#!/usr/bin/python3
""" returns the Json representation of an object """
import json


def to_json_string(my_obj):
    """ function to return Json """
    data = json.dumps(my_obj)
    return data
