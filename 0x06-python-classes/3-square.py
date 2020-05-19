#!/usr/bin/python3
""" this is a module """


class Square:
    """ Defines a Square class """
    def __init__(self, size=0):
        """ initializes Square with optional value of 0 - size will be private
        Args:
            size: size of Square
        Raises:
            TypeError: if size is not of type int
            ValueError: if size is less than 0
        """
        if isinstance(size, int):
            pass
        else:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ calls area function to calculate Square area
        Returns: current square area
        """
        return self.__size ** 2
