#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
def add_integer(a, b=98):
   """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """ 
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")
return int(a) + int(b)
