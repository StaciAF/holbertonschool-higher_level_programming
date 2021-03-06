#!/usr/bin/python3
"""
this module adds a method to check if object is instance of class or inhertance
"""


def inherits_from(obj, a_class):
    """ this method checks if obj is instance of same class as inherited
    Args:
        obj: the object passed for comparison
        a_class: the class to be compared against
    Returns:
        True if object is inherited instance else, False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
