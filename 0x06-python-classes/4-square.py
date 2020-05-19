#!/usr/bin/python3
""" no modules imported """


class Square:
    """ Defines a Square class """
    def __init__(self, size=0):
        """ initializes Square with optional value of 0 - size will be private
        Args:
            size: size of Square
        """
        self.__size = size

    @property
    def size(self):
        """ defines properties of size making attribute private
        Returns: private instance of size
"""
        return self.__size

    @size.setter
    def size(self, value):
        """ defines size setter
        Raises:
            TypeError: if size/value is not of type int
            ValueError: if size/value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ defines public function to get Square area
        Returns: area of current Square
        """
        return self.size ** 2
