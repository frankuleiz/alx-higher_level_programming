#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return None
    return {x: value * 2 for x, value in a_dictionary.items()}
