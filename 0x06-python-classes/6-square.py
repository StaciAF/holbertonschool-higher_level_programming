#!/usr/bin/python3
""" no modules imported """


class Square:
    """ Defines a Square class with private attribute size """
    def __init__(self, size=0, position=(0, 0)):
        """ initializes class with size attribute
        Args:
        size: size of Square (int)
        position: position of Square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ sets the position property for Square as private
        Returns: private instance of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the position of Square """
        tup_error = 'position must be a tuple of 2 positive integers'
        if type(value) is tuple and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if (value[0] >= 0 and value[1] >= 0):
                    self.__position = value
                else:
                    raise TypeError(tup_error)
            else:
                raise TypeError(tup_error)
        else:
            raise TypeError(tup_error)

    def area(self):
        """ defines public method to calculate area of square
        Returns: the current Square's area
        """
        return self.size ** 2

    def my_print(self):
        """ defines public print method to output a sqaure at position """
        i = 0
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
