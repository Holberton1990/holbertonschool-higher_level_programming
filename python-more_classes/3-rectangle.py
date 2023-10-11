#!/usr/bin/python3
class Rectangle:
    """
    __init__ - inicializon një klasë drejtkëndëshi

    Args:
        width (int): gjërësia e drejtkëndëshit
        height (int): lartësia e drejtkëndëshit
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("gjërësia duhet të jetë një numër të plotë")
        if value < 0:
            raise ValueError("gjërësia duhet të jetë >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("lartësia duhet të jetë një numër të plotë")
        if value < 0:
            raise ValueError("lartësia duhet të jetë >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
