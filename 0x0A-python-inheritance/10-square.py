#!/usr/bin/python3
"""
The ``10-square'' module
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
