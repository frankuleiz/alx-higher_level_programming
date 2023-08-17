#!/usr/bin/pyhton3
def complex_delete(a_dictionary, value):
    """
    function that deletes keys with a specific value in a dictionary
    If the value doesn’t exist, the dictionary won’t change
    All keys having the searched value have to be deleted
    """
    for key, val in sorted(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]
    return a_dictionary
