#!/usr/bin/python3
"""This module contains an inherit fuction"""


def inherits_from(obj, a_class):
    """
        A function that returns True if an object is a subclass of a specified\
        class else returns False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
