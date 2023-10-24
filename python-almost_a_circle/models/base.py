#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base.__nb__objects
 
 class Rectangle():

    def area(self):
        return self.__height * self__width