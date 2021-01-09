#!/usr/bin/python3
'''
Module for add integer function
'''


def add_integer(a, b=98):
    '''Function that adds 2 integers'''

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
