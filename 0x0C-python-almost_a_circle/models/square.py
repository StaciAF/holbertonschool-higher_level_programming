#!/usr/bin/python3
""" this module creates square class that inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines Square class with Rectangle inheritance """
    def __init__(self, size, x=0, y=0, id=None):
        """ this method initializes Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ this method initializes string representation of Square class """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """ returns public instance of size """
        return self.width

    @size.setter
    def size(self, value):
        """ this PUBLIC method sets the value of width/height to size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ PUBLIC method that assigns arguments to attributes """
        if len(args) != 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j

        else:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key == 'size':
                    self.size = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        """ this PUBLIC method returns dictionary rep of Square """
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["size"] = self.size
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict
