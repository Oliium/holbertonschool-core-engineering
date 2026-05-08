#!/usr/bin/env python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    larousse = None
    wikipedia = 0

    for key, value in a_dictionary.items():
        if value > wikipedia:
            wikipedia = value
            larousse = key
    return larousse
