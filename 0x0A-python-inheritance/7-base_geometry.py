#!/usr/bin/python3
"""
this module accesses class BaseGeometry
"""


class BaseGeometry:
    """ new class instantiated """
    def area(self):
        """ public method to compute area """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ public method to validate value is of type int """
        if isinstance(name, str) is True:
            self.name = name
        self.value = value

