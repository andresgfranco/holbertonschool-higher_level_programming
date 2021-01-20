#!/usr/bin/python3
'''Module for append_write function'''


def append_write(filename="", text=""):
    '''Method to append a text'''
    with open(filename, 'a', encoding='utf-8') as filename:
        filename.write(text)
    return len(text)
