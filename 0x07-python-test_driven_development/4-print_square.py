#!/usr/bin/python3
"""
This module prints a square with the character #.
The size argument must be of type integer and can not be less than zero
"""


def print_square(size):
    """ checks for integer type of size, prints square with size as length """
    size_error = "size must be an integer"
    zero_error = "size must be >= 0"
    if isinstance(size, int) is False:
        raise TypeError(size_error)
    if isinstance(size, float) is True:
        raise TypeError(size_error)
    if size < 0:
        raise ValueError(zero_error)
    for x in range(size):
        print('#' * size)
