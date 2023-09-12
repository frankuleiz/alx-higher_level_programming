#!/usr/bin/python3
"""The ``3-to_json_string``"""
import json


def to_json_string(my_obj):
    """
    Function to change a string to a json representation

    Args:
        my_object: the object to print as json

    Return:
        The json representation of a string
    """
    return json.dumps(my_obj)
