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
        """
        The setter method of __size
        Args:
            value: the size value to be set
        Return: None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints the square with character # in stdout
        or an empty line if 0
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
