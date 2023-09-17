#!/usr/bin/python3
"""The ``square`` module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class definition of Square that inherits from the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the square object instance 
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        A function that sets the size of the square instance
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        The setter method for the atttribute size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        A function that updates the square object instances passed
        passed as arguments
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
        A function that returns a string representation of the square
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__,
                self.id, self.x, self.y, self.width)


