#!/usr/bin/python3
"""
This module prints 'My name is <first_name> <last_name>'.
Both first_name and last_name must be given as strings
"""


def say_my_name(first_name, last_name=""):
    """ checks for both arguments to be strings, prints sentence """
    first_error = "first_name must be a string"
    last_error = "last_name must be a string"
    if isinstance(first_name, str) is False:
        raise TypeError(first_error)
    if isinstance(last_name, str) is False:
        raise TypeError(last_error)
    print("My name is {} {}".format(first_name, last_name))
