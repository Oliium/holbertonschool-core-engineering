#!/usr/bin/env python3
"""Definition d'un carré avec getter et setter pour size."""


class Square:
    """Representation d'un carré avec acces controle a size."""
    def __init__(self, size=0):
        """Initialise le carré via le setter (validation centralisee)."""
        self.size = size

    @property
    def size(self):
        """Getter : retourne la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : valide puis assigne la taille du carré."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré (size * size)."""
        return self.__size ** 2
