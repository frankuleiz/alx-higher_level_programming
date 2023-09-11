#!/usr/bin/python3
""" The is a ``2-is_same_class``module"""


def is_same_class(obj, a_class):
    """
        A fuction that returns True if obj is an instance of a specified class
    """

    return (type(obj) is a_class)
