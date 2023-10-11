#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
def add_integer(a, b=98):
    """
    python3 -c 'print(__import__("my_module").__doc__)'
    """ 
    if type(a)  not isinstance(int, float):
        raise TypeError("a must be an integer")
    if type(b) not isinstance(int, float):
        raise TypeError("b must be an integer")
    return int(a) + (b)
