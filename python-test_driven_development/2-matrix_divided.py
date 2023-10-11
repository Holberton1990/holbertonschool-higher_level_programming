#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
def matrix_divided(matrix, div):
    """
    python3 -c 'print(__import__("my_module").__doc__)'
    """
    if matrix not isinstance(int, float)
        raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                    )

    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(
                        "matrix must be a matrix "
                        "(list of lists) of integers/floats"
                        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
