#!/usr/bin/python3
'''Script hat adds all arguments
to a Python list, and then save them to a file'''
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
i = len(argv)

try:
    list_arguments = load_from_json_file("add_item.json")
except:
    list_arguments = []

for counter in range(1, i):
    list_arguments.append(argv[counter])

save_to_json_file(list_arguments, "add_item.json")
