#!/usr/bin/python3
"""
The ``8-rectangle`` module.
It defines the class BaseGeometry of subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representation of a rectangle"""

    def __init__(self, width, height):
        """Initializes the rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
