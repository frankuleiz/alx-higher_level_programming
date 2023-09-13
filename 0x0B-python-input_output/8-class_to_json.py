#!/usr/bin/python3
"""The ``8-class_to_json`` module"""


def class_to_json(obj):
    """
    A function that creates a dictionary description for json serialization

    Args:
        obj: object to create a dictionary

    Return:
        dictionary description
    """
    return obj.__dict__
