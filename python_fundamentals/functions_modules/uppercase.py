#!/usr/bin/env python3
def uppercase(str):
    for alphabet in str:
        if ord('a') <= ord(alphabet) <= ord('z'):
            alphabet = ord(alphabet) - 32
            alphabet = chr(alphabet)
        print("{}".format(alphabet), end='')
    print()
