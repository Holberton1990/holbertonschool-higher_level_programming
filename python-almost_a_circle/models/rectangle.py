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
    return self._width
@width.setter
def width(self, value):
    if width is not int:
        raise TypeError(" width must be an integer")
    if width < 0:
        return ValueError("width must be >= 0")
self.__width = width

@property
def height(self):
    return self.__height
@height.setter
def height(self, value):
     if height is not int:
            raise TypeError("height must be an integer")
    if height < 0:
        return ValueError("height must be >= 0")
    self.__height = height

@property
def x(self):
    return self.__x
@width.setter
def x(self, value):
     if x is not int:
            raise TypeError("x must be an integer")
    if x < 0:
        return ValueError("x must be >= 0")
    self.__x = x 

@property
def y(self):
    return self._y
@y.setter
def y(self, value):
    if y is not int:
            raise TypeError("y must be an integer")
    if y < 0:
        return ValueError("y must be >= 0")
    self.__y = y

 class Rectangle():
    """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
        
    def area(self):
        return self.__height * self__width

class Rectangle():
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    def display(self):