#!/usr/bin/python3
'''
Module for text_indentation function
'''


def text_indentation(text):
    '''Function that a text with 2 new lines
    after each of these characters: .,? and :
    '''

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ('.', '?', ':'):
            print("{}\n".format(text[i]))
            if i + 1 < len(text):
                while text[i + 1] == " ":
                    i += 1
        else:
            print(text[i], end='')
        i += 1
