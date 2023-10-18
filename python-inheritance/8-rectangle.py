#!/usr/bin/python3

class Rectangle(BaseGeometry):
        '''
    Class that inherits from list class
    '''
    def __init__(self, width, height):
               '''
        Init function for Rectangle class
        '''
        BaseGeometry.integer_validator(self, width, width):
        BaseGeometry.integer_validator(self, height, height):
        self._width = width
        self._height = height
    