#!/usr/bin/python3
'''Module for class Student'''


class Student():
    '''Class Student that defines
    a student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        for i in attrs:
            if type(i) is not str:
                return self.__dict__
        my_dict = {}
        for i in attrs:
            if i in self.__dict__:
                my_dict[i] = self.__dict__.get(i)
        return my_dict
