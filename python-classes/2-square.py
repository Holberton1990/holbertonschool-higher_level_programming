#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""
class Square:
    """
    This is the documentation for the Square class.
    The class represents a geometric square and associated operations.
    """
def __init__(self, size=0):
    """
    python3 -c 'print(__import__("my_module").__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif:
        raise ValueError("size must be >=0")
    self.__size = size
