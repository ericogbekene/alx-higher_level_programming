import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    """
    test cases for square
    """

    def test_square(self):
        """ test square method """
        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 2)

    def test_square_area(self):
        """ testing the return of Area """
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

        #self.assertEqual(print(s3), '[Square] (3) 1/3 - 3')
