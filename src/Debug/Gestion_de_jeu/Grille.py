import numpy as ny

LARGEUR = 7
LONGEUR = 6

class Grille:
    """
        Commentaire sur la classe
    """

    def __init__(self, g_longueur, g_largeur):
        """ Commentaire sur la fonction """
        self.grille = ny.empty((g_longueur, g_largeur), dtype=object)

    def remplir_grille(self, g_numero_colonne, g_jeton):
        """ Commentaire sur la fonction """
        self.grille[0][g_numero_colonne] = g_jeton

    def coup_valide(self):
        """ Commentaire sur la fonction """
        pass
