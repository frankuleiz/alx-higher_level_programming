#!/usr/bin/python3
"""
The ``0-read_file`` module"""


def read_file(filename=""):
    """
    Function that reads text file and prints to stdout
    Args:
        filename: text file to be read

    Return:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')
