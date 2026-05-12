#!/usr/bin/env python3
"""Definition de la classe Square, fille de Rectangle."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Carré : rectangle dont width == height == size."""
    def __init__(self, size):
        """Valide size puis initialise le Rectangle parent avec size, size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Retourne l'aire du carre (size * size)."""
        return self.__size ** 2
