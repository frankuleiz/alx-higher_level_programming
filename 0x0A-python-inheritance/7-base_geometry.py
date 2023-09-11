#!/usr/bin/python3
"""A definition of ``BaseGeometry`` class"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """A function that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            A function that validates whether value is an integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
