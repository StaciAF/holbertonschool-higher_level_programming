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
        new_dict = {}
        if type(attrs) == list:
                for value in attrs:
                    if value in list(self.__dict__.keys()):
                        new_dict[value] = self.__dict__[value]
                return new_dict
        else:
            return self.__dict__
