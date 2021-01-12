#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Class with private instance att"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve a property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set if this conditions"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve a property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set if this conditions"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Retuns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0

        else:
            return 2 * (self.__height + self.__width)
