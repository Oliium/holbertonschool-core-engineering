#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    le_first = tuple_a[:2] + (0, 0)
    le_second = tuple_b[:2] + (0, 0)
    return (le_first[0] + le_second[0], le_first[1] + le_second[1])
