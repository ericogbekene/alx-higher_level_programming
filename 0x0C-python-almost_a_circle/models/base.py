#!/usr/bin/python3
""" creating the Base class for the project """
import json


class Base:
    """ defining the base class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instanstiates an instance """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns a jsonstring"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            data = json.loads(list_dictionaries)
            return data
