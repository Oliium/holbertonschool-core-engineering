#!/usr/bin/env python3
"""Definition d'un carré avec pour objectif une taille restant privé."""


class Square:
    """representation d'un carré avec taille restant privé."""
    def __init__(self, size):
        self.__size = size
