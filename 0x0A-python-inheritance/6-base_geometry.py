#!/usr/bin/python3
"""A definition of ``BaseGeometry`` class"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """A function that raises an exception"""
        raise Exception("area() is not implemented")
