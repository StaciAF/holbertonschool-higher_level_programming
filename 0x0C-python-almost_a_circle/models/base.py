#!/usr/bin/python3
"""
this module initializes Base class
"""
import json


class Base:
    """
    defines class Base with private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes Base class
        Args:
            id: object id if not None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        this method returns JSON representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        this method writes JSON string to a file
        """
        saved_file = str(cls.__name__) + ".json"
        if list_objs is None:
            with open(saved_file, "w") as json_file:
                json.dump("[]", json_file)
        else:
            for obj in list_objs:
                ob_file = []
                ob_file.append(cls.to_dictionary(obj))
        with open(saved_file, "w") as json_file:
            written = json_file.write(cls.to_json_string(ob_file))
        return written

    @staticmethod
    def from_json_string(json_string):
        """ this method returns the JSON string representation of argument """
        this_list = []
        if json_string is None or json_string == "":
            return this_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ this method returns an instance with attributes set """
        pass

    @classmethod
    def load_from_file(cls):
        """ this method returns a list of instances """
        pass
