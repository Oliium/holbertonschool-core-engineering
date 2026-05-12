#!/usr/bin/env python3
"""Definition d'un rectangle avec width et height privees."""


class Rectangle:
    """Representation d'un rectangle avec acces controle a ses dimensions."""
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
