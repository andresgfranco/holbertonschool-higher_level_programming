#!/usr/bin/python3
'''
Module for divide function
'''


def matrix_divided(matrix, div):
    '''Function that divides all elements of a matrix '''

    # matrix evaluation #
    Error_string = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(Error_string)

    if len(matrix) < 1:
        raise TypeError(Error_string)

    if not (all(isinstance(element, list) for element in matrix)):
        raise TypeError(Error_string)

    for row in matrix:
        if len(row) < 1:
            raise TypeError(Error_string)
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError(Error_string)

    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            continue

    # div evaluation #
    if (type(div) != int and type(div) != float) or div is None:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_list = []
        for i in row:
            new_list.append(round((i / div), 2))
        new_matrix.append(new_list)
    return (new_matrix)
