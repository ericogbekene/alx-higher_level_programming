#!/usr/bin/python3
""" function to append text to a file """


def append_write(filename="", text=""):
    """ this function will append text to a file """

    with open(filename, "a") as newfile:
        return newfile.write(text)
