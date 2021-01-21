#!/usr/bin/python3
'''Module for the write_file method'''


def write_file(filename="", text=""):
    '''Method to write a file'''
    with open(filename, 'w+', encoding='utf-8') as filename:
        return(filename.write(text))
