#!/usr/bin/env python3
for alphabet in (range(97, 123)):
    if alphabet != 101 and alphabet != 113:
        print(chr(alphabet), end='\n' if alphabet == 122 else '')
