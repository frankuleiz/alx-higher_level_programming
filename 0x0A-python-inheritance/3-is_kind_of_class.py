#!/usr/bin/python3
"""A ``3-is_kind_of_class``module"""


def is_kind_of_class(obj, a_class):
    """
        A function that returns True if the object is an instance or has\
        inherited from a specified class else returns False
    """
    return (isinstance(obj, a_class))
