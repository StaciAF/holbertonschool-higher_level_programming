#!/usr/bin/python3
""" no modules imported """


class Square:
    """ Defines Square class """
    def __init__(self, size=0):
        """ defines size attribute for Square, attribute will be private """
        self.__size = size

    @property
    def size(self):
        """ defines properties os size making attribute private
        Returns: private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size to value
        Raises:
            TypeError if size/value is not integer
            ValueError if size/value less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ defines method to find area of current Square
        Returns: the area of the current Square
        """
        return self.size ** 2

    def __eq__(self, other):
        return ((self.size) == (other.size))

    def __ne__(self, other):
        return ((self.size != other.size))

    def __lt__(self, other):
        return ((self.size < other.size))

    def __le__(self, other):
        return ((self.size <= other.size))

    def __gt__(self, other):
        return ((self.size > other.size))

    def __ge__(self, other):
        return ((self.size >= other.size))
