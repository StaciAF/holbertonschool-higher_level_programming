#!/usr/bin/python3
"""
this module initializes Base class
"""


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
