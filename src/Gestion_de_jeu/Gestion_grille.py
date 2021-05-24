import numpy as ny
import Gestion_jeton

class Grille:
    """
        Cette classe permet de gérer le plateau de jeu sous forme matricielle.
    """

    def __init__(self, g_ligne, g_colonne):
        """
            Cette méthode est le constructeur de la classe Grille.
            
            Paramètres :
                g_ligne : variable de type entier correspondant on nombre de lignes de la matrice
                g_colonne : variable de type entier correspondant on nombre de colonnes de la matrice
        """

        self.grille = ny.empty((g_ligne, g_colonne), dtype=object)
        self.ligne = g_ligne
        self.colonne = g_colonne

    def coup_valide(self, g_num_colonne):
        """
            Cette méthode permet de vérifier si un coup joué est valide ou non.

            Paramètre :
                g_num_colonne : entier correspondant à la colonne du coup joué
            
            Retourne :
                un booléen : True si le coup est valide, False sinon.
        """

        return (self.grille[0][g_num_colonne] is None)

    def coup_gagnant(self, couleur):
        """
            Cette méthode permet de vérifier si un coup gagant a été joué dans la grille
            en fonction de la couleur du jeton passé en paramètre.

            Paramètre :
                couleur : entier correspondant à la couleur du jeton 
                            1 : rouge
                            2 : jaune

            Retourne :
                un booléen : True si un coup gagnant a été trouvé, False sinon
        """

        for ligne in range(self.ligne):
            for colonne in range(self.colonne-3):
                jeton1 = self.grille[ligne][colonne]
                jeton2 = self.grille[ligne][colonne+1]
                jeton3 = self.grille[ligne][colonne+2]
                jeton4 = self.grille[ligne][colonne+3]

                if((jeton1 is not None) and (jeton2 is not None) and (jeton3 is not None) and (jeton4 is not None)):
                    if(jeton1.couleur == jeton2.couleur == jeton3.couleur == jeton4.couleur == couleur):
                        return True

        for ligne in range(self.ligne-3):
            for colonne in range(self.colonne):
                jeton1 = self.grille[ligne][colonne]
                jeton2 = self.grille[ligne+1][colonne]
                jeton3 = self.grille[ligne+2][colonne]
                jeton4 = self.grille[ligne+3][colonne]

                if((jeton1 is not None) and (jeton2 is not None) and (jeton3 is not None) and (jeton4 is not None)):
                    if(jeton1.couleur == jeton2.couleur == jeton3.couleur == jeton4.couleur == couleur):
                        return True

        for ligne in range(self.ligne-3):
            for colonne in range(self.colonne-3):
                jeton1 = self.grille[ligne][colonne]
                jeton2 = self.grille[ligne+1][colonne+1]
                jeton3 = self.grille[ligne+2][colonne+2]
                jeton4 = self.grille[ligne+3][colonne+3]    

                if((jeton1 is not None) and (jeton2 is not None) and (jeton3 is not None) and (jeton4 is not None)):
                    if(jeton1.couleur == jeton2.couleur == jeton3.couleur == jeton4.couleur == couleur):
                        return True

        for ligne in range(3,self.ligne):
            for colonne in range(self.colonne-3):
                jeton1 = self.grille[ligne][colonne]
                jeton2 = self.grille[ligne-1][colonne+1]
                jeton3 = self.grille[ligne-2][colonne+2]
                jeton4 = self.grille[ligne-3][colonne+3]    

                if((jeton1 is not None) and (jeton2 is not None) and (jeton3 is not None) and (jeton4 is not None)):
                    if(jeton1.couleur == jeton2.couleur == jeton3.couleur == jeton4.couleur == couleur):
                        return True
        
        return False
    
    def est_pleine(self):
        """
            Cette méthode vérifie si la grille est pleine en regardant le nombre de jetons.

            Retourne :
                un booléen : True si la grille est remplie, False sinon
        """

        return (Gestion_jeton.Jeton.nombre_jeton == (self.ligne*self.colonne))

    def vider_grille(self):
        """
            Cette méthode permet de remettre à "None" toutes les cases de la grille.
        """

        for i in range(self.ligne):
            for j in range(self.colonne):
                if(self.grille[i][j] is not None):
                    self.grille[i][j] = None
    
    def remplir_grille(self, g_contenu_grille):
        """
            Cette méthode permet de remplir une grille à partir d'une chaîne de caractères
            passée en paramètre.

            Paramètre :
                g_contenu_grille : chaîne de caractère correspondant à un contenu de grille
        """

        i = 0
        j = 0

        for jeton in g_contenu_grille:
            if(jeton != '0'):
                self.grille[i][j] = Gestion_jeton.Jeton(int(jeton))
            j += 1

            if(j%self.colonne == 0):
                j = 0
                i += 1
