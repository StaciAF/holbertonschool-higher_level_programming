#!/usr/bin/python3
""" no modules imported """


class Square:
    """ Defines a Square class with private attribute size """
    def __init__(self, size=0):
        """ initializes class with size attribute
        Args: size: size of Square (int)
        """
        self.__size = size

    @property
    def size(self):
        """ defines properties of size making size attribute private
        Returns: private instance of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ defines size setter function
        Raises:
            TypeError: if size/value is not an integer
            ValueError: if size/value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ defines public method to calculate area of square
        Returns: the current Square's area
        """
        return self.size ** 2

    def my_print(self):
        """ defines public print method to output a sqaure """
        i = 0
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
