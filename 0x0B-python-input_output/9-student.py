#!/usr/bin/python3
"""The ``9-studnt`` module"""


class Student:
    """Defines a class student"""

    def __init__(self, first_name, last_name, age):
        """A method that initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A method that retrieves dictionary representation of a student"""
        return self.__dict__
