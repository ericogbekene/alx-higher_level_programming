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

    def area(self):
        """ return the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ to return the details of the rectangle """
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)
