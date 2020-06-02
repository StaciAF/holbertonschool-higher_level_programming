#!/usr/bin/python3
"""
this module adds method to check class and subclass
"""


def is_kind_of_class(obj, a_class):
    """ method checks if object is instance of class or inherited class """
    return(isinstance(obj, a_class))
