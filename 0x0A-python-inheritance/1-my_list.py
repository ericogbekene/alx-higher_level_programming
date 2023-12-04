#!/usr/bin/python3
""" a class Mylist that inherits from list """


class MyList(list):
    """ defines a class MyList that inherits from list """
    def __init__(self):
        """ init method """
        pass

    def print_sorted(self):
        """ prints out sorted list """
        print(sorted(self))
