#!/usr/bin/python3
""" this is a module """


class Square:
    """ Defines a Square class """

    def __init__(self, size=0):
        """ initialize Square with private size and optional value of 0
        Args:
            size: size of Square
        Raises:
            TypeError: if size is not an intger
            ValueError: if size is less than 0
"""
        if isinstance(size, int):
            pass
        else:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
