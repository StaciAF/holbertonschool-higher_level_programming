#!/usr/bin/python3
"""
this module with define Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ instantiates Square inheriting Rectangle
    Args:
        size: size of Square, private instance
    """

    def __init__(self, size):
        """ this module makes size private """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ this module calculates Square area """
        return (self.__size ** 2)

    def __str__(self):
        """ returns and prints string representation """
        return ("[" + str(__class__.__name__) + "]" + " {}/{}".format
                (self.__size, self.__size))
