#!/usr/bin/python3
"""
This module sums two arguments, both must be of type integer or type float
Float must be converted to integer before addition
"""


def add_integer(a, b=98):
    """ checks input, converts float to integer, return sum of two integers """
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    elif isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
