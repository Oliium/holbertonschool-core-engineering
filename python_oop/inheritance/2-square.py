#!/usr/bin/env python3
"""Square avec sa propre representation __str__."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Carré avec affichage personnalise [Square] <width>/<height>."""
    def __init__(self, size):
        """Valide size puis initialise le Rectangle parent avec size, size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Retourne l'aire du carre (size * size)."""
        return self.__size ** 2

    def __str__(self):
        """Retourne la representation [Square] <size>/<size>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
