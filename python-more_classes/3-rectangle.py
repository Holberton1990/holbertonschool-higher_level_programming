#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

@property
def width(self):
    #Getter function for width
    return self.__width

@property
def width(self, value):
    #Setter function for width
    if not isinstance(value, int):
        return TypeError("width must be an integer")
    if value < 0:
        return ValueError("width must be >= 0")    
    return self.__width = value

@property
def height(self):
    return self.__height

@property
def height(self, value)
    if not isinstance(value, int):
        return TypeError("height must be an integer")
    if value < 0:
        return ValueError("height must be >= 0")
    return self.__height = value

def area(self):
    return self.__height * self.__width

def perimeter(self):
    if self.__width == 0 or self.__height == 0:
        return 0
    return 2 * (self.__height * self._width)

def __str__(self):
    if self.__width == 0 or self.__height == 0:
        return " "
    return "\n".join(["#" + self.__width] * self.__height)
def __repr__(self):
    return f"Rectangle({self.__width}, {self.__height})" 
