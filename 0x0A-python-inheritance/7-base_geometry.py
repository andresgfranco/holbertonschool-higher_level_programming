#!/usr/bin/python3
'''Module for class BaseGeometry'''


class BaseGeometry():
    '''class BaseGeometry'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Check if value is a positive integer'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
