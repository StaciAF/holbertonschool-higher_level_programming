#!/usr/bin/python3
""" this module writes a class Rectangle then defines it """


class Rectangle:
    """ defines Rectangle class """

    def __init__(self, width=0, height=0):
        """ initialize Rectangle with width attribute
        Args:
            width: width of Rectangle
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ defines private instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ defines width setter function
        width must be of type integer, must be >= 0
        """
        w_int_error = "width must be an integer"
        w_val_error = "width must be >= 0"
        if isinstance(value, int) is False:
            raise TypeError(w_int_error)
        if value < 0:
            raise ValueError(w_val_error)
        self.__width = value

    @property
    def height(self):
        """ defines private instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ defines height setter function
        height must be of type integer, must be >= 0
        """
        h_int_error = "height must be an integer"
        h_val_error = "height must be >= 0"
        if isinstance(value, int) is False:
            raise TypeError(h_int_error)
        if value < 0:
            raise ValueError(h_val_error)
        self.__height = value

    def area(self):
        """ this method returns the area of the Rectangle """
        return self.width * self.height

    def perimeter(self):
        """ this method returns the perimeter of the Rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.height + self.width))

    def __str__(self):
        """ this method returns and prints the string representation """
        rec_string = ""
        if self.width == 0 or self.height == 0:
            return(rec_string)
        for y in range(self.height):
            for x in range(self.width):
                rec_string += '#'
            rec_string += '\n'
        rec_string = rec_string[:-1]
        return rec_string

    def __repr__(self):
        """ this method returns a printable version of Rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
