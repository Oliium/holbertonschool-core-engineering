#!/usr/bin/env python3
"""Definition d'un carré avec size, position et representation textuelle."""


class Square:
    """Representation d'un carré affichable avec offset et __str__."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialise size et position via leurs setters (validation)."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter : retourne la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter : valide qu'il s'agit d'un tuple de 2 entiers positifs."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retourne l'aire du carré (size * size)."""
        return self.__size ** 2

    def __str__(self):
        """Retourne le carré sous forme de chaîne, avec offset."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        row = " " * self.__position[0] + "#" * self.__size
        lines.extend([row] * self.__size)
        return "\n".join(lines)

    def my_print(self):
        """Affiche le carré (delegue a __str__ via print)."""
        print(self)
