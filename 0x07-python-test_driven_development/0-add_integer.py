#!/usr/bin/python3
"""
This module sums two arguments, both must be of type integer or type float
Float must be converted to integer before addition
"""


def add_integer(a, b=98):
    """ checks input, converts float to integer, return sum of two integers """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
