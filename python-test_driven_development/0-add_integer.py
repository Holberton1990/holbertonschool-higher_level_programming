#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
    a (int or float): The first number.
    b (int or float, optional): The second number. Default is 98.

    Returns:
    int: The sum of a and b as an integer.

    Raises:
    TypeError: If a or b is not an int or float.
    """
    if type(a)  not isinstance(int, float):
        raise TypeError("a must be an integer")
    if type(b) not isinstance(int, float):
        raise TypeError("b must be an integer")
    
a = int(a)
b = int(b)

    return a + b
