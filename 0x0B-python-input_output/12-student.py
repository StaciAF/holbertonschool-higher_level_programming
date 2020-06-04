#!/usr/bin/python3
"""
this module defines a class Student with public instance attributes
"""


class Student:
    """ defines class Student """

    def __init__(self, first_name, last_name, age):
        """ initializes public attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ this method retrieves dict represenation of Student """
        if attrs is None:
            return self.__dict__
        for items in attrs:
            if items:
                return self.__dict__.items()
