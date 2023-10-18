#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

class MyList(list):

def print_sorted(self):
    """
    'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    sorted_list = sorted(self)
    print (sorted_list(self))
    return sorted_list
