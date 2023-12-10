import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    """

    creating a class of test case
    that inherits from unittest.testcase

    """

    def testing_base(self):
        """

        method to test the base class
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)
