#!/usr/bin/python3
"""Defines a class of Rectangle"""


class Rectangle:

    def __init__(self, width=0, height=0):
        """
    A class rectangle definition.
    The rectangle with private attributes width and  height
    """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter method of __width
        Args:
            value: gets the value of height
        Return: None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter method to retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter method of __height
        Args:
            value: the value of height
        Return: None
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
