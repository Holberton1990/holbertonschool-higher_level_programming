#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """
python3 -c 'print(__import__("my_module").__doc__)'
"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super()._init_(size, size)
        self._size = size

    def area(self):
        return self._size ** 2
