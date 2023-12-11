#!/usr/bin/python3
""" define a class rectangle from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class
        that inherits from Base

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ define width """
        return self.__width

    @width.setter
    def width(self, width=0):
        """ method to set width """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """ method to get height """
        return self.__height

    @height.setter
    def height(self, height=0):
        """ method to set height """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter of attribute x """
        return self.__x

    @x.setter
    def x(self, x=0):
        """ method to set x """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter for attribute y """
        return self.__y

    @y.setter
    def y(self, y=0):
        """ method to set y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        public method to define area of a rectangle
        """

        return (self.__width * self.__height)

    def display(self):
        """
        public method to diplay # in a rectangle

        """
        for count in range(self.y):
            print()
        for num in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ print a string representation """

        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ update the function with varying number of arguments

        """
        """
        if len(args) < 1:
            raise ValueError("Enter at least 1 argument for update")
        elif len(args) > 5:
            raise ValueError("Too many arguments passed")
        """
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.width = args[1] if len(args) > 1 else self.width
            self.height = args[2] if len(args) > 2 else self.height
            self.x = args[3] if len(args) > 3 else self.x
            self.y = args[4] if len(args) > 4 else self.y
            """
            logic to use kwargs
            """
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ method to return a dict representation of Rectangle"""
        """return self.__dict__ """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
