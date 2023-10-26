#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        super().__init__(size, size, x, y, id)

 
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs)
    list_arguments = ["id", "size", "x", "y"]

    if args or args != "[]":
        for idx in range(len(args)):
            seattr(self, atributtes[idx], args[idx])
    else:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

        
    @classmethod
    def load_from_file(cls):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        file = cls.__name__ + ".json"
        l_inst = []
        try:
            with open(file, "r") as f:
                l_dict = Base.from_json_string(f.read())
                for d_item in l_dict:
                    inst = cls.create(**d_item)
                    l_inst.append(inst)
            return l_inst
        except FileNotFoundError:
            return []