#!/usr/bin/python3
""" The ``4-from_json_string`` module"""
import json


def from_json_string(my_str):
    """
    Function to decode to a json string to an object

    Args:
        my_string: the string to decode

    Return:
        an object represented by a json string
    """
    return json.loads(my_str)
