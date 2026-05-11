#!/usr/bin/env python3
def safe_print_division(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        resultat = None
        return resultat
    finally:
        print("Inside result: {}".format(resultat))
    return resultat
