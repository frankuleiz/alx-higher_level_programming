#!/usr/bin/python3
"""A ``base`` module class"""
import os
import sys


class Base:
    """
    A base class deifinition

    Attributes:
        __nb_objects: the number of instances of Base class

    Methods:
        __init__()
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class

        Args:
            id(int): The object instance identity
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
