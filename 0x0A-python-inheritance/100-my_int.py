#!/usr/bin/python3
"""
The ``100-my_int`` module
"""


class MyInt(int):
    """
        A class definition of an inverted equality operator
        """
    def __new__(cla, *args, *kwargs):
        return super(MyInt, cls).__new__(cls, *args, *kwargs)

    def __eq__(self, other):
        """A function for equality operator"""
        return int(self) != other

    def __ne__(self, other):
        """A function for checking enequality operator"""
        return int(self) == other
