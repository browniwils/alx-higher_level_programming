#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ Print integer in multi dimentional list """
    for mat in matrix:
        for m in mat:
            if mat.index(m) == len(mat) - 1:
                print("{:d}".format(m), end="")
            else:
                print("{:d}".format(m), end=" ")
        print()
