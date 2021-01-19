#/usr/bin/python3
'''Module for the lookup function'''
def lookup(obj):
    '''Return the list of available
    attributes and methods of an object '''
    list_attributes = list(dir(obj))
    return list_attributes
