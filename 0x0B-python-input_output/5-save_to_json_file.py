#!/usr/bin/python3
""" save an object to Json file """
import json


def save_to_json_file(my_obj, filename):
    """ this function saves an object to json file """

    with open(filename, "w") as save_file:
        json.dump(my_obj, save_file)
