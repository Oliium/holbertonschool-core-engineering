#!/usr/bin/env python3
"""Definition d'un carré avec calcul de l'aire."""


class Square:
    """Representation d'un carré avec une methode area()."""
    def __init__(self, size=0):
        """Initialise le carré en validant le type et la valeur de size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Retourne l'aire du carré (size * size)."""
        return self.__size ** 2
