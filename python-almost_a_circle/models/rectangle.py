#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
from models.base import Base

class Rectangle(Base):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.__width = width
        self.__height = height
        self.__x = x 
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError(" width must be an integer")
        if value < 0:
            return ValueError("width must be >= 0")
            self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
    @width.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            return ValueError("x must be >= 0")
        self.__x = value 

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            return ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.height * self.width


    def display(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        print("\n" * self.y, end="")
        for h in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """   
        return "[Rectangle] {} {}/{} - {}/{}".format(self.id, self.width, self.y, self.height, self.x) 

    def update(self, *args, **kwargs):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        attributes = ['id', 'width', 'heigh', 'x', 'y']


        if args:
            for idx in range(len(args)):
                setattr(self, attributes[idx], args[idx])
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        
    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
    