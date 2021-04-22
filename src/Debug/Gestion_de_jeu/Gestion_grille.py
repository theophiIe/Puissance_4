import numpy as ny
import Puissance_4/src/Gestion_de_Jeu/Gestion_jeton

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
        if(ny.size(self.grille) == 0):
            return False

        if(self.grille[0][g_num_colonne] is None):
            return True

        return False

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
        if(ny.size(self.grille) == 0):
            return False

        num_ligne = 5
        for i in range(0,6):
            if(self.grille[i][g_num_colonne] is not None):
                num_ligne = i
        
        for i in range(-3,1):
            ligne = num_ligne + i
            ligne_inverse = num_ligne - i
            colonne = g_num_colonne + i

            if((ligne > -1) and (ligne < 3)):
                jeton1 = self.grille[ligne][g_num_colonne]
                jeton2 = self.grille[ligne+1][g_num_colonne]
                jeton3 = self.grille[ligne+2][g_num_colonne]
                jeton4 = self.grille[ligne+3][g_num_colonne]
                if((jeton1 is not None) and (jeton2 is not None) and (jeton3 is not None) and (jeton4 is not None)):
                    if(jeton1.couleur == jeton2.couleur == jeton3.couleur == jeton4.couleur):
                        return True

            if((colonne > -1) and (colonne < 4)):
                jeton1 = self.grille[num_ligne][colonne]
                jeton2 = self.grille[num_ligne][colonne+1]
                jeton3 = self.grille[num_ligne][colonne+2]
                jeton4 = self.grille[num_ligne][colonne+3]
                if((jeton1 is not None) and (jeton2 is not None) and (jeton3 is not None) and (jeton4 is not None)):
                    if(jeton1.couleur == jeton2.couleur == jeton3.couleur == jeton4.couleur):
                        return True

            if(((ligne > -1) and (ligne < 3)) and ((colonne > -1) and (colonne < 4))):
                jeton1 = self.grille[ligne][colonne]
                jeton2 = self.grille[ligne+1][colonne+1]
                jeton3 = self.grille[ligne+2][colonne+2]
                jeton4 = self.grille[ligne+3][colonne+3]
                if((jeton1 is not None) and (jeton2 is not None) and (jeton3 is not None) and (jeton4 is not None)):
                    if(jeton1.couleur == jeton2.couleur == jeton3.couleur == jeton4.couleur):
                        return True

            if(((ligne_inverse > 2) and (ligne_inverse < 6)) and ((colonne > -1) and (colonne < 4))):
                jeton1 = self.grille[ligne_inverse][colonne]
                jeton2 = self.grille[ligne_inverse-1][colonne+1]
                jeton3 = self.grille[ligne_inverse-2][colonne+2]
                jeton4 = self.grille[ligne_inverse-3][colonne+3]
                if((jeton1 is not None) and (jeton2 is not None) and (jeton3 is not None) and (jeton4 is not None)):
                    if(jeton1.couleur == jeton2.couleur == jeton3.couleur == jeton4.couleur):
                        return True

        return False
    
    def est_pleine(self):
        """
           Cette méthode permet de vérifier si la grille de jeu est pleine.
           Cette méthode renvoie un booléen.
           True si la grille est pleine, False sinon.
        """
        if(Jeton.nombre_jeton >= 42):
            return True
        return False

    def vider_grille(self):
        """
            Cette méthode permet de vider la grille
            en remettant toutes les cases de la matrice
            à none.
        """
        for i in range(6):
            for j in range(7):
                if(self.grille[i][j] is not None):
                    self.grille[i][j] = None
        pass
    
    def remplir_grille(self, g_contenu_grille):
        """
            Cette méthode permet de remplir la grille
            grâce à la chaîne de caractères passée en argument.
            
            Cette méthode ne renvoie rien.
        """
        i = 0
        j = 0
        for jeton in g_contenu_grille:
            if(jeton != '0'):
                self.grille[i][j] = Jeton(jeton)
            j += 1
            if(j%7 == 0):
                j = j%7
                i += 1
        pass
