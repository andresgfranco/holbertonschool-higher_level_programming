#!/usr/bin/python3
'''Module for the class Base'''
import json
import csv


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

        if list_dictionaries is None or not list_dictionaries:
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
        filename = "{}.json".format(cls.__name__)

        if list_objs is None:
            with open(filename, 'w') as file_class:
                file_class.write("[]")
        else:
            dict_list = []
            for i in range(0, len(list_objs)):
                dict_list.append(list_objs[i].to_dictionary())
                dict_list = cls.to_json_string(dict_list)

            with open(filename, 'w') as file_class:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Serializes in CSV'''
        filename = cls.__name__ + ".csv"
        my_dict_list = []

        if cls.__name__ == 'Rectangle':
            attrs = ["id", "width", "height", 'x', 'y']
        if cls.__name__ == "Square":
            attrs = ["id", "size", 'x', 'y']
        for my_objs in list_objs:
            my_dict_list.append(cls.to_dictionary(my_objs))

        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=attrs)
            writer.writeheader()
            writer.writerows(my_dict_list)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        my_dict_list = []

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                res = {key: int(val) for key, val in row.items()}
                my_dict_list.append(cls.create(**res))
            return my_dict_list
