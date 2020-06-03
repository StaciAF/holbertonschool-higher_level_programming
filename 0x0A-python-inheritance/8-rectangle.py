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
