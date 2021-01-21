#!/usr/bin/python3
'''Module for the method save_to_json_file'''
import json


def save_to_json_file(my_obj, filename):
    '''Method from json to file'''
    with open(filename, 'w') as filename:
        json.dump(my_obj, filename)
