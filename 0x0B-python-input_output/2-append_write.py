#!/usr/bin/python3
"""The ``2-append`` module """


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a file

    Args:
        filename: the file to append and write
        text: the content of the file

    Return:
        number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
