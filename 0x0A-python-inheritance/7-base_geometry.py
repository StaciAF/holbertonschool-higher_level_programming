#!/usr/bin/python3
"""
this module accesses class BaseGeometry
"""


class BaseGeometry:
    """ new class instantiated """

    def area(self):
        """ public method to compute area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public method to validate value is of type int """
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
