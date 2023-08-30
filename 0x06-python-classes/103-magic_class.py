#!/usr/bin/python3
"""Defines MagicClass"""
import math


class MagicClass:
    """
    This is a representation of a circle
    Circle has private attribute radius
    """
    def __init__(self, radius):
        """
        Initializes th MagicClass
        Args:
            radius: radius of the circle
        Return: None
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """calculats the circumference of the circle"""
        return math.pi * 2 * self.__radius
