#!/usr/bin/python3
"""
This is 4-print_square module.
It prints a square passed as an argument
"""


def print_square(size):
    """
    A function that prints a square

    Args:
        size: the size of the square as an int
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size >= 0:
        for i in range(size):
            print('#' * size)
    elif size < 0:
        raise ValueError("size must be >= 0")
