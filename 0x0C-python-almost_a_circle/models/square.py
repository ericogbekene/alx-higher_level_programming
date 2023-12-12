#!/usr/bin/python3
""" defining a square sub inheritance class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ init method of the square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation overide"""

        return "[Square] ({:d}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ public getter for size"""

        return (self.width)

    @size.setter
    def size(self, size):
        """ setter method for square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be > 0")
        self.size = size
        """self.height = size"""

    def update(self, *args, **kwargs):
        """ method to update attributes"""

        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.size = args[1] if len(args) > 1 else self.width
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary representation of Square"""

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
