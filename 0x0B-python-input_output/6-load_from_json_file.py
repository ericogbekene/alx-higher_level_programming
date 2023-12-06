#!/usr/bin/python3
""" loading a python file onject """
import json


def load_from_json_file(filename):
    """ this will create an object from a json file """
    with open(filename, "r") as file_object:
        my_object = json.load(file_object)
        return my_object
