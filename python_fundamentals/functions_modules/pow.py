#!/usr/bin/env python3
def pow(a, b):
    resultat = 1
    le_pouvoir = abs(b)

    for ma_puissance in range(le_pouvoir):
        resultat *= a

    if b < 0:
        return 1 / resultat
    return resultat
