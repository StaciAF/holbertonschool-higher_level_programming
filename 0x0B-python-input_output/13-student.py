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

    def to_json(self):
        """ this method retrieves dict represenation of Student """
        return self.__dict__
