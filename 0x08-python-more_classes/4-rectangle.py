#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
"""


class Rectangle:
    """ Class To Define a Rectangle with withd and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return to the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Return to rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ Print the rectangle with the character # """
        if self.__height == 0 or self.__width == 0:
            return ("")
        return ("\n".join(("#" * self.__width for i in range(self.__height))))

    def __repr__(self):
        """ Return a string representation of the rectangle to be able to
            recreate a new instance by using eval()"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
