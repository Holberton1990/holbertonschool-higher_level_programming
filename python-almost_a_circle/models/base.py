#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


import json


class Base:
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    def save_file(cls, list_objs):

        if list_objs is None:
            list_objs = []
            for obj in list_objs:
                l_dict.append(obj.to_dictionary())
        with open("cls.name",  "json", "w") as file:
            f.write(cls.to_json_string(l_dict)) 
