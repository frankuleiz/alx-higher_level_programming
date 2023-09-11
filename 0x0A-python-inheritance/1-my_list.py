#!/usr/bin/python3

class MyList(list):
    """The ``1-my_list`` module"""

    def __init__(self):
        """A subclass of list"""
        self.list = list

    def print_sorted(self):
        """function that prints a sorted list"""
        print(sorted(self))
