#!/usr/bin/python3
"""The ```Rectangle``` module """


from models.base import Base


class Rectangle(Base):
    """
    Defines the Rectangle class that inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle object instances"""
        super()__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        The getter method of private attribute width
        Args:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter method of attribute width
        Args:
            Value: new value of the width of the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        The getter method of private attribute height
        Args:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter method of attribute height
        Args:
        Value: new value of the height of the rectangle
        """
        self.__height = value

