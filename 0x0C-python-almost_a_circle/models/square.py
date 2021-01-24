#!/usr/bin/python3
'''Module for class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square that inherits
    from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}/{}".format\
                (self.id, self.x, self.y, self.width, self.height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update the class Square attributes'''
        if len(args) > 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                    self.height = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
