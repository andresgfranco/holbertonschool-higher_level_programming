#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i matrix:
        for count, j in enumerate(i):
            print("{:d}".format(j), end='')
            if count != (len(matrix) - 1):
                print(" ", end='')
        print("")
