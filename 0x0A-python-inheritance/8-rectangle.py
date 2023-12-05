#!/usr/bin/python3
""" area exception based on Geometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class retangle inheriting from Base Geometry """

    def __init__(self, width, height):
        """ instantiates a new retangle object """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
