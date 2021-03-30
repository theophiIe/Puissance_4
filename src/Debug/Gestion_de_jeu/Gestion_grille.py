import numpy as ny

class Grille:
    """
        Classe Grille permet de gérer la grille de jeu
        cette grille est représentée par une matrice contenant
        des objets de type Jeton ou objet none s'il n'y a pas de Jeton 
    """

    def __init__(self, g_ligne, g_colonne):
        """
            Constructeur de la classe Grille.

            Ce constructeur permet d'initialiser un matrice vide de type object
            de taille g_longueur par g_largeur.

            Paramètre :
                g_ligne   : nombre de lignes de la grille de type entier positif
                g_colonne : nombre de colonnes de la grille de type entier positif
        """
        self.grille = ny.empty((g_ligne, g_colonne), dtype=object)

    def coup_valide(self, g_num_colonne):
        """
            Cette méthode permet de vérifier si le coup est valide ou non. 
            Pour cela, on regardera si la colonne où le coup
            doit être joué est pleine.

            Paramètre:
                g_num_colonne : correspond au numéro de colonne où le coup veut être joué
                                le paramètre est de type entier

            Renvoie: bool
                true si le coup est valide
                false si le coup n'est pas valide
        """
        pass

    def coup_gagnant(self, g_num_colonne):
        """
            Cette méthode permet vérifier si le coup qui vient d'être joué
            est un coup gagnant ou non en vérifiant si 4 jetons de la même
            couleur sont alignés.

            Paramètre:
                g_num_colonne : correspond au numéro de colonne où le coup a été joué
                                le paramètre est de type entier


            Renvoie: bool
                true si on a un quadruplet de jetons de la même couleur
                false si le coup n'est pas gagnant
        """
        pass

    def vider_grille(self):
        """
            Cette méthode permet de vider la grille
            en remettant toutes les cases de la matrice
            à none.
        """
        pass
