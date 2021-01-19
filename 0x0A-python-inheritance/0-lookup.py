#!/usr/bin/python3
'''Module for the lookup function'''


def lookup(obj):
    '''Return the list of available
    attributes and methods of an object '''
    return list(dir(obj))
