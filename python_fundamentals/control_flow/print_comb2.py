#!/usr/bin/env python3
for chiffre in (range(0, 100)):
    print('{:02d}'.format(chiffre), end=', ' if chiffre != 99 else '\n')
