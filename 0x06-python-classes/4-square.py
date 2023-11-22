#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """
        initializimg class

        Args:
            size - of Square
        """
        self.__size = size

    def size(self):
        """
        function for size
        """
        return self.__size

    def size(self, value=0):
        """
        property setter for size

        Args:
            self - instance
            value - of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current area of a sqaure """

        return self.__size ** 2
