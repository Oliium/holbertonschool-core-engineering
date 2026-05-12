#!/usr/bin/env python3
"""Definition de la classe Rectangle, fille de BaseGeometry."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle valide via le integer_validator herite de BaseGeometry."""
    def __init__(self, width, height):
        """Initialise width et height en validant via le parent."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
