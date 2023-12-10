#!/usr/bin/python3
""" creating the Base class for the project """


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
