#!/usr/bin/env python3
def print_last_digit(number):
    terminus = abs(number) % 10
    print("{}".format(terminus), end='')
    return terminus
