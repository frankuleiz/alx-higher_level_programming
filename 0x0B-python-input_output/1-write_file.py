#!/usr/bin/python3
"""The ``1-write`` module"""


def write_file(filename="", text=""):
    """
    A function that writes to a text file

    Args:
        filename: the file to be written
        text: the content to write

    Return:
        number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
