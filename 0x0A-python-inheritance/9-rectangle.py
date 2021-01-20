#!/usr/bin/python3
'''Module for Rectangle class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle that
    inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''Instantiation'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("heigth", height)
        self.__height = height

    def area(self):
        '''Function to calculate area'''
        return self.__width * self.__height

    def __str__(self):
        '''Method that returns to a description about this class'''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
