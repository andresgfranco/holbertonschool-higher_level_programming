#!/usr/bin/python3
'''Module to create a class called MyList'''


class MyList(list):
    '''Class that inherits from list'''
    def print_sorted(self):
        '''Method to print a list of sorted integers'''
        print(sorted(self))
