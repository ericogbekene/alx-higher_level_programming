import unittest

from models.base import Base

from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """

    class to test rectangle

    """
    def testing_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        """
        check raise exception

        r4 = Rectangle("a", 10)
        self.assertRaises(ValueError, r4.id)
        """
