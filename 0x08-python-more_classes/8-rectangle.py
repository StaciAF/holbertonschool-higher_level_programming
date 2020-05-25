#!/usr/bin/python3
""" this module writes a class Rectangle then defines it """


class Rectangle:
    """ defines Rectangle class """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1
        self.print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ this method returns the biggest rectangle based on area """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """ this method returns and prints the string representation """
        rec_string = ""
        if self.width == 0 or self.height == 0:
            return(rec_string)
        for y in range(self.height):
            for x in range(self.width):
                rec_string += str(self.print_symbol)
            rec_string += '\n'
        rec_string = rec_string[:-1]
        return rec_string

    def __repr__(self):
        """ this method returns a printable version of Rectangle """
        return "Rectangle({:d},{:d})".format(self.width, self.height)

    def __del__(self):
        """ this method prints at deletion """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        return Rectangle.number_of_instances
