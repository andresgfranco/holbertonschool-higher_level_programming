#!/usr/bin/python3
'''Module for read file method'''


def read_file(filename=""):
    '''Function to read a file'''
    with open(filename, mode='r', encoding='utf-8') as filename:
        print(filename.read(), end="")
