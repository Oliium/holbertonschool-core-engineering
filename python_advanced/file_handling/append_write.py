#!/usr/bin/env python3
"""Module pour ajouter du texte à la fin d'un fichier."""


def append_write(filename="", text=""):
    """Ajoute une chaîne en fin de fichier et retourne le nbre de caractères"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
