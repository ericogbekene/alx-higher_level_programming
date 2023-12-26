#!/usr/bin/python3
""" defining a student class """


class Student:
    """ a student class """

    """
    Public Attributes
    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """ init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary representation of student"""
        return self.__dict__

