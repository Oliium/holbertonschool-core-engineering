#!/usr/bin/env python3
"""Module pour lire un fichier texte et l'afficher sur la sortie standard."""


def read_file(filename=""):
    """Lit un fichier UTF-8 et affiche son contenu."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
