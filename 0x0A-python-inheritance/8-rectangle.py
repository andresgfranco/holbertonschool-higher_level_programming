#!/usr/bin/python3
'''Module for Rectangle class'''


class BaseGeometry():
    '''class BaseGeometry'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''function to validate if is an integer
        or not'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''Class Rectangle that
    inherits from BaseGeometry'''
    def __init__(self, width, height):
        self.integer_validator("heigth", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
