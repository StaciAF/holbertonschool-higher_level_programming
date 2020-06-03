#!/usr/bin/python3
"""
this module creates Rectangle class inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ instantiates class Rectangle inheriting """

    def __init__(self, width, height):
        """ initalizes Rectangle instance
        Args:
            width: private attribute of Rectangle
            height: private attribute of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calculates area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns and prints string representation """
        return ("[" + str(__class__.__name__) + "]" + " {}/{}".format
                (self.__width, self.__height))
