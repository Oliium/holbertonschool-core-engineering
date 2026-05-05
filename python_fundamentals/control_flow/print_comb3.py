#!/usr/bin/env python3
for digit in (range(0, 10)):
    for digit2 in (range(digit+1, 10)):
        separateur = ', ' if digit*10+digit2 != 89 else '\n'
        print('{:02d}'.format(digit*10+digit2), end=separateur)
