#!/usr/bin/python3
"""
The '3-say_my_name' module.
This module passes one function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints first and last name

    Args:
        first_name: the users's first name of type string
        last_name: the user's last ane of type string

    Return: user's full name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
