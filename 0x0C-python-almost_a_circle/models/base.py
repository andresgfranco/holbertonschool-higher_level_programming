#!/usr/bin/python3
'''Module for the class Base'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of
        list_dictionaries'''

        if list_dictionaries is None or len(list_dictionaries) <= 0:
                return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the JSON string
        representation json_string'''

        if json_string is None or len(json_string) <= 0:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of
        list_objs to a file'''

        if list_objs is None:
            list_objs = []
        else:
            dict_list = []

            for i in range(0, len(list_objs)):
                dict_list.append(list_objs[i].to_dictionary())
            dict_list = cls.to_json_string(dict_list)

        with open("{}.json".format(cls.__name__), 'w') as file_class:
            file_class.write(dict_list)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes
        already set'''

        dummy = cls(1, 1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        filename = cls.__name__ + ".json"
        json_string = ""
        list_instances = []

        try:
            with open(filename) as fl:
                json_string = fl.read()
        except FileNotFoundError:
            return list()

        list_from_json = cls.from_json_string(json_string)
        for i in list_from_json:
            list_instances.append(cls.create(**i))

        return list_instances
