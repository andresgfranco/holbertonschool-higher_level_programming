#!/usr/bin/python3
'''Module for the from_json_string method'''
import json


def from_json_string(my_str):
    '''Method to convert from json to string'''
    return json.loads(my_str)
