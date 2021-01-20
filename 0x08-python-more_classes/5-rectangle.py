#!/usr/bin/python3
""" class Rectangle """


class Rectangle():
    """ defines a rectangle """
    def __init__(self, width=0, height=0):
        """ initializate a new objet """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def gheight(self):
        """ gets the height """
        return self.__height

    def sheight(self, value):
        """ sets the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    height = property(gheight, sheight)

    def area(self):
        """ return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ return the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ return a string of the rectangle with the character # """
        x = ""
        if self.__width == 0 or self.__height == 0:
            return x
        for i in range(1, self.__height):
            x += "#" * self.__width + "\n"
        x += "#" * self.__width
        return x

    def __repr__(self):
        """ return a string representation of a rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ prints a message and decrement the number of instances """
        print("Bye rectangle...")
