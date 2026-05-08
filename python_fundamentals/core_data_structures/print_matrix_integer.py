#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
        else:
            for element in range(0, len(row)):
                if element == len(row) - 1:
                    print("{:d}".format(row[element]))
                else:
                    print("{:d}".format(row[element]), end=" ")
