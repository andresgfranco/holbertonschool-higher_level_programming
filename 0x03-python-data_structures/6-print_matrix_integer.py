#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
            for i in matrix:
                for count, j in enumerate(i):
                    print("{:d}".format(j), end='')
                    if count != (len(matrix) - 1):
                        print("{:s}".format(" "), end='')
                print("")
    else:
        print("")
