#!/usr/bin/env python3
"""Definition de la classe de base BaseGeometry."""


class BaseGeometry:
    """Classe de base pour les formes geometriques."""
    def area(self):
        """Leve une exception car non implementee dans la classe de base."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que value est un entier strictement positif."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
