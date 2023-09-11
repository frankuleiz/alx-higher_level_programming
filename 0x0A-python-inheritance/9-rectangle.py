#!/usr/bin/python3

"""A definition of ``BaseGeometry`` class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class representation of a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """A function that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This is a string representation of the rectangle"""
        return f"[{:s}] {:d}/{:d}"
