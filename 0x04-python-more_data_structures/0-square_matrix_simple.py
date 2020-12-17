#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    new_matrix = list(map(list, matrix))
    for count_1, i in enumerate(matrix):
        for count_2, j in enumerate(i):
            new_matrix[count_1][count_2] = j * j     
    return(new_matrix)
