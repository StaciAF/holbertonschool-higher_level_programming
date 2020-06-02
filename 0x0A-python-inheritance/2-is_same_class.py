#!/usr/bin/python3
"""
this module adds method to check if two objects are instances of the same class
"""


def is_same_class(obj, a_class):
    """ this method checks for instances of a given class """
    if (type(obj) is a_class):
        return True
    else:
        return False
