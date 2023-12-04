#!/usr/bin/python3
""" area exception based on Geometry class """


class BaseGeometry:
    """ base class Geometry """

    def area(self):
        """ defines an area public method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value """
        if type(value) is not int:
            raise TypeError("{} must be be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
