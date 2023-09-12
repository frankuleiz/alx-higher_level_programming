#!/usr/bin/python3
"""The ``5-save_to_json_file``"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function to write an object to a text file using json

    Args:
        my_object: the object to be written in json
        filename: the text file

    Return:
        Json representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
