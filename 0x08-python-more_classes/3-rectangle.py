#!/usr/bin/python3
"""
Module 1-rectangle
Defines a rectangle class
"""


class Rectangle:
    """
    Defines class Rectangle

    Methods:
        __init__(): creates an object instance
        width(): width attribute
        height(): height atttribute
    """

    def __init__(self, width=0, height=0):
        """
        A method that initializes a Rectangle instance

        Args:
            width: the width size of the rectangle
            height: the height size of the rectangle
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter method to retrieve width of the rectangle

        Return:
            width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to get the value of the width

        Args:
            Value: an int value of the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method  to get the value of the height

        Return:
            height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The getter method to update the value of height

        Args:
            value: an int value of the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        A method that calculates and returns the area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        A method tha calculates and returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        A method that returns string representation of rectangle
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                string += "#" * self.__width
                if i + 1 != self.__height:
                    string += "\n"

        return string
