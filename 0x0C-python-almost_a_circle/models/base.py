#!/usr/bin/python3
"""A ``Base`` module class"""
import json
import csv


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
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(3, 2)

            else:
                dummy = cls(2)

            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        A function that returns a list of instances depending on the class
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                dicts_list = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in dicts_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        A function that writes to a file in csv format
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
