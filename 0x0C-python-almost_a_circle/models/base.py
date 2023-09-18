#!/usr/bin/python3
"""A ``Base`` module class"""


class Base:
    """
    A base class deifinition

    Attributes:
        __nb_objects: the number of instances of Base class

    Methods:
        __init__()
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class

        Args:
            id(int): The object instance identity
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        A function that returns the json string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A function that writes a json string representation to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        A function that deserializes a json string representation
        Returns:
            A json list of the json string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    
    @classmethod
    def create(cls, **dictionary):
        """
        A fuction that creates a class instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 2)

        if cls.__name__ == "square":
            dummy = cls(2)

        dummy.update(**dictionary)
        return dummy
