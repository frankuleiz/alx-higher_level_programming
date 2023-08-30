#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class square definition
    square with private attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square instance
        Args:
            size: size of the square
            position: position of the square
        Return: None
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        The setter  method of __position
        Args:
            value: represent the value in a tuple
        Return: None
        """
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        """
        Prints the square with character # in stdout
        or an empty line if 0
        """
        if self.__size == 0:
            print()
            return
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
