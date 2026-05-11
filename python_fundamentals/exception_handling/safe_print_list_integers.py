#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for interger in range(x):
            if isinstance(my_list[interger], int):
                print("{:d}".format(my_list[interger]), end="")
                counter += 1
        print()
    except TypeError:
        pass
    return counter
