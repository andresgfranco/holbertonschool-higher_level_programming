#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
            for i in matrix:
                for count, j in enumerate(i):
                    if count == (len(matrix) - 1):
                        print("{:d}".format(j))
                    else:
                        print("{:d} ".format(j), end='')
    else:
        print('')
