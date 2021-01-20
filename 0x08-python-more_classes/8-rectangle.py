#!/usr/bin/python3
""" class Rectangle """


class Rectangle():
    """ defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        symbol = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return x
        for i in range(1, self.__height):
            x += symbol * self.__width + "\n"
        x += symbol * self.__width
        return x

    def __repr__(self):
        """ return a string representation of a rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ prints a message and decrement the number of instances """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        area1 = 0
        area2 = 0

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 == area2:
            return rect_1
        if area1 > area2:
            return rect_1
        else:
            return rect_2
