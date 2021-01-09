#!/usr/bin/python3
'''
Module for print_square function
'''


def print_square(size):
    '''Function that prints
    a square with the character #
    '''

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for row in range(size):
        for i in range(size):
            print("#", end='' if i+1 != size else '\n')
