#!/usr/bin/env python3
"""Definition d'un carré avec affichage via my_print()."""


class Square:
    """Representation d'un carré affichable avec des #."""
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

    def my_print(self):
        """Affiche le carré avec des #. Ligne vide si size == 0."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
