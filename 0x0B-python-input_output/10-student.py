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
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            if i in self.__dict__ and type(i) is str:
                new_dict[i] = self.__dict__.get(i)
        return new_dict
