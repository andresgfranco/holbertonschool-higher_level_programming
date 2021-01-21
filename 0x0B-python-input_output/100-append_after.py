#!/usr/bin/python3
'''Module for the append_after method'''


def append_after(filename="", search_string="", new_string=""):
    '''Method that inserts a line of text to a file,
    after each line containing a specific string'''
    with open(filename, "r") as inp:
        new_file_lines = []
        for line in inp:
            if search_string in line:
                line = line + new_string
                new_file_lines.append(line)
            else:
                new_file_lines.append(line)
    with open(filename, 'w') as new_document:
        new_document.writelines(new_file_lines)
