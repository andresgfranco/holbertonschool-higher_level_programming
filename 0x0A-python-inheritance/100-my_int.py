#!/usr/bin/python3
'''Module for class MyInt'''


class MyInt(int):
    '''Class MyInt that
    inherits from int'''
    def __eq__(self, other):
        """ invert """
        return False

    def __ne__(self, other):
        """ invert """
        return True
