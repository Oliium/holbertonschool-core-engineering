#!/usr/bin/env python3
"""Module pour écrire dans un fichier texte."""


def write_file(filename="", text=""):
    """Écrit une chaîne dans un fichier UTF-8 et retourne le nombre de caractères."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
