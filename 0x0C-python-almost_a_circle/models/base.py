#!/usr/bin/python3
'''Module for the class Base'''


class Base():
    '''This class will be the "base" of all
    other classes in this project. It will manage
    id attribute in all the future classes and to avoid duplicating
    the same code'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects = self.id
