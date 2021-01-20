#!/usr/bin/python3
'''Module for the write_file method'''


def write_file(filename="", text=""):
    with open(filename, 'w+', encoding='utf-8') as filename:
        filename.write(text)
    return (len(text))
