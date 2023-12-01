#!/usr/bin/python3
""" function to auto indent """


def text_indentation(text):
    """ a function to add indentation to a text

        Args:
            text - a string of text

        raises:
            TypeError - if argument is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i == ".":
            print()
            print()
            pass
        elif i == "?":
            print()
            print()
        elif i == ":":
            print()
            print()
        else:
            print(i.lstrip(), end='')
