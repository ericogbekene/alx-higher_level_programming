#!/usr/bin/python3
""" a function to write to a text file """


def write_file(filename="", text=""):
    """ writes to a file

    Args:
        filename: to write to
        text: to write into the file
    """

    with open(filename, "w") as file:
        return file.write(text)
