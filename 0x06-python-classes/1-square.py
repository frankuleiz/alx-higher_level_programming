#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """
    A class Square definition
    Square with private attribute size
    """
    def __init__(self, size):
        """
        Initializes a new square instance
        Args:
            size: size of the square
        Return: None
        """
        self.__size = size
