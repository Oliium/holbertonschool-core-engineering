#!/usr/bin/env python3
"""Definition d'un rectangle avec calcul d'aire et de perimetre."""


class Rectangle:
    """Representation d'un rectangle avec methodes area et perimeter."""
    def __init__(self, width=0, height=0):
        """Initialise width et height via leurs setters (validation)."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter : retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter : valide puis assigne la largeur du rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter : retourne la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter : valide puis assigne la hauteur du rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle (width * height)."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le perimetre du rectangle (0 si une dimension est 0)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
