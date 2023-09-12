#!/usr/bin/python3
"""The ``6-load_from_json_file`` module"""
import json


def load_from_json_file(filename):
    """
    A function that creates an object from a json file

    Args:
        filename: the json file

    Return:
        a python data structure(object)
    """
    with open(filename, 'r') as f:
        return json.load(f)
