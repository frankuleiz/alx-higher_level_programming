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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        The getter method of private attribute height
        Args:
            height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter method of attribute height
        Args:
        Value: new value of the height of the rectangle
        """
        self.__height = value

    @property
    def x(self):
        """
            getter function for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x.
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            getter function for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        A function that prints the instance of rectangle as #
        """
        print("\n" * self.__y, end="")

        for i in range(self.__height):
            print("{:s}{:s}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """Function that overides the __str__"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.__class__.__name__,
                self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """A function that updates the attributes of the rectangle"""
        attr = ["id", "width", "height", "x", "y"]

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except Exception:
            pass

    def to_dictionary(self):
        """
        A function that returns the square attributes as a dictionary
        """
        return {"id": self.id,
                "width": self.width,
                "height": self.width,
                "x": self.x,
                "y": self.y}
