import numpy as ny

class Grilles:
    """
        Commentaire sur la classe
    """

    def __init__(self, g_longueur, g_largeur):
        """ Commentaire sur la fonction """
        self.grille = ny.empty((g_longueur, g_largeur), dtype=object)

    def coup_valide(self, g_num_colonne):
        """ Commentaire sur la fonction """
        pass

    def coup_gagnant(self, g_num_colonne):
        """ Commentaire sur la fonction """
        pass

    def vider_grille(self):
        """ Commentaire sur la fonction """
        pass
