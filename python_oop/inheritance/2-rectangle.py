#!/usr/bin/env python3
"""Rectangle avec area() et representation __str__."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle qui implemente area() et son affichage."""
    def __init__(self, width, height):
        """Initialise width et height en validant via le parent."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Retourne l'aire du rectangle (width * height)."""
        return self.__width * self.__height

    def __str__(self):
        """Retourne la representation [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
