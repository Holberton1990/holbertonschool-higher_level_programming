#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class BaseGeometry:
   """
python3 -c 'print(__import__("my_module").__doc__)'
"""
def area(self):
    '''
        Instance method to raise an Exception
        '''
    raise Exception("area() is not implemented")
def integer_validator(self, name, value):
    '''
    Fubction for checking an valid integer
    '''
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")
    if type(value) <= 0:
        raise TypeError(f"{name} must be grater than 0")
