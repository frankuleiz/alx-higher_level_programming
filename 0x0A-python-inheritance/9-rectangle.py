#!/usr/bin/python3

"""A definition of ``BaseGeometry`` class"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """A function that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            A function that validates whether value is an integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is a class representation of a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """A function that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This is a string representation of the rectangle"""
        return "[Rectangle] {:d} / {:d}".format(self.__width, self.__height)

