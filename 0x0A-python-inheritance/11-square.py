#!/usr/bin/python3
"""
The ``11-square'' module.
It has the class BaseGeometry and subclass Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""

    def __init__(self, size):
        """Initializes the instance of asquare"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """A function that returns the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """This is a string representation of a square"""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
