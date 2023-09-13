#!/usr/bin/python3
"""The ``100-append_after``module"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text to a file

    Args:
        filename: the file to insert file
        search_string: the specific string
        new_string: the string to be inserted

    Return:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        s = ""
        for line in f:
            s += line
            if search_string in line:
                s += new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(s)
