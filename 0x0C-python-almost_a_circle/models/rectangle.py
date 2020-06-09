#!/usr/bin/python3
"""
this module initializes Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    defines class Rectangle with Base inheritance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes Rectangle class
        Args:
            width: width of rectangle
            height: height of rectangle
            x: coordinate for rectangle
            y: coordinate for rectangle
            id: id of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ PUBLIC method - defines width as private attribute
        Returns: private instance of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width, validates value
        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        w_int_err = "width must be an integer"
        w_val_err = "width must be > 0"
        if type(value) != int:
            raise TypeError(w_int_err)
        if value <= 0:
            raise ValueError(w_val_err)
        self.__width = value

    @property
    def height(self):
        """ PUBLIC method - defines height as private attribute
        Returns: private instance of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height, validates value
        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        h_int_err = "height must be an integer"
        h_val_err = "height must be > 0"
        if type(value) != int:
            raise TypeError(h_int_err)
        if value <= 0:
            raise ValueError(h_val_err)
        self.__height = value

    @property
    def x(self):
        """ PUBLIC method - defines x as public attribute
        Returns: public instance of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets x, validates value
        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        x_int_err = "x must be an integer"
        x_val_err = "x must be >= 0"
        if type(value) != int:
            raise TypeError(x_int_err)
        if value < 0:
            raise ValueError(x_val_err)
        self.__x = value

    @property
    def y(self):
        """ PUBLIC method - defines y as public attribute
        Returns: public instance of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y, validates value
        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        y_int_err = "y must be an integer"
        y_val_err = "y must be >= 0"
        if type(value) != int:
            raise TypeError(y_int_err)
        if value < 0:
            raise ValueError(y_val_err)
        self.__y = value

    def area(self):
        """ PUBLIC method area
        Returns: the area value of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ PUBLIC method display that prints Rectangle with # """
        rec_string = ""
        for i in range(self.__y):
            print()
        for i in range(self.__x):
            rec_string += " "
        for i in range(self.__width):
            rec_string += str('#')
        for j in range(self.__height):
            print(rec_string)

    def __str__(self):
        """ this method will override current __str__
        Returns:
            updated format str for object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ PUBLIC method at assigns arguments to attributes """
        if len(args) != 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.width = j
                if i == 2:
                    self.height = j
                if i == 3:
                    self.x = j
                if i == 4:
                    self.y = j

        else:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key == 'width':
                    self.width = val
                if key == 'height':
                    self.height = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        """ this PUBLIC method returns dictionary rep of Rectangle """
        rec_dict = {}
        rec_dict["id"] = self.id
        rec_dict["width"] = self.width
        rec_dict["height"] = self.height
        rec_dict["x"] = self.x
        rec_dict["y"] = self.y
        return rec_dict
