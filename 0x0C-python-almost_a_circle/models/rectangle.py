#!/usr/bin/python3
'''Module for class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle that inherits
    from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width (self):
        return self.__width

    @width.setter
    def width (self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator('y', value)
        self.__y = value

    @staticmethod
    def validator(name, value):
        '''Validate if value is int and if it's more,
        less or equal than 0'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''Returns the area value of the Rectangle instance'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print('#', end="")
            print()
