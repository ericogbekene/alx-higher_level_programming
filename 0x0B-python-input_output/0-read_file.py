#!/usr/bin/python3
""" a function to read from a file nd print to output """


def read_file(filename=""):
    """ module to open and read a file """

    with open(filename, 'r') as file:
        output = file.read()
        print(output)
