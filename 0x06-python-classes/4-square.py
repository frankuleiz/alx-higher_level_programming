#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class square definition
    square with private attribute size
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance
        Args:
            size: size of the square
        Return: None
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
