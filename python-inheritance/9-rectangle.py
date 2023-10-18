#!/usr/bin/python3
'''
Python simple module
for demonstarative purpose
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class that inherits from list class
    '''
    def __init__(self, width, height):
        '''
        Init function for Rectangle class
        '''
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
