#!/usr/bin/python3
"""The ``10-student`` module"""


class Student:
    """Defines a class student"""

    def __init__(self, first_name, last_name, age):
        """A method that initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A method that retrieves a dictionary representation of a student
        Args:
            attrs: string to be retrieved of specified attributes

        Return:
            a dictionary 
        """
        if attrs is None:
            return self.__dict__
        new_dict = self.__dict__
        return {k: new_dict[k] for k in attrs and new_dict.keys()}
