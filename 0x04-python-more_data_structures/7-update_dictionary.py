#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    a function that replaces or adds key/value in a dictionary
    a function that replaces or adds key/value in a dictionary.
    value argument will be any type
    If a key exists in the dictionary, the value will be replaced
    If a key doesn’t exist in the dictionary, it will be created
    """
    a_dictionary[key] = value
    return a_dictionary
