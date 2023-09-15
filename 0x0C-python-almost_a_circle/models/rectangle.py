#!/usr/bin/python3
"""The ```Rectangle``` module """
from models.base import Base


class Rectangle(Base):
    """
    Defines the Rectangle class that inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle object instances"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        The getter method of private attribute width
        Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter method of attribute width
        Args:
            Value: new value of the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        The getter method of private attribute height
        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter method of attribute height
        Args:
            Value: new value of the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if <= 0:
            raise ValueError("height > 0")
        self.__height = value

    @property
    def x(self):
        """
        The getter method of private attribute x
        Return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        The setter method of private attribute of x
        Args:
            Value: the new value of x
        """
        self.__x = value

    @property
    def y(self):
        """
        The getter method of private atttribute of y
        Return: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        The setter method of private attribute of y
        Args:
            Value: the new value of y
        """
        self.__y = value
