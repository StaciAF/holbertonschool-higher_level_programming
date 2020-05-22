#!/usr/bin/python3
"""
This modules divides all elements of a matrix
Matrix must be a list of lists with values of types integer and float
Each matrix row must be the same size
Dividend results should be rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """ checks matrix as list, checks for value types, returns new matrix
    Args:
        matrix: matrix given to be divided
        div: number given to be divided by, must be int/float
    """
    int_error = "matrix must be a matrix (list of lists) of integers/floats"
    row_error = "Each row of the matrix must have the same size"
    divNum_error = "div must be a number"
    zero_error = "division by zero"

    if len(matrix) is 0:
        raise TypeError(int_error)
    if isinstance(matrix, list) is False:
        raise TypeError(int_error)
    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError(int_error)
        for x in row:
            if isinstance(x, (int, float)) is False:
                raise TypeError(int_error)
    if isinstance(div, (int, float)) is False:
        raise TypeError(divNum_error)
    if div is 0:
        raise ZeroDivisionError(zero_error)
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError(row_error)
    return[[round(x/div, 2) for x in row] for row in matrix]
