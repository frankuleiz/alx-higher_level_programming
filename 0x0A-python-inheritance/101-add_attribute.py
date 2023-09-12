#!/usr/bin/python3
"""
The  ``101-add_attribute`` module
"""


def add_attribute(obj, attr, value):
    """A function that sets attributes"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
