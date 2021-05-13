import numpy as ny
import Gestion_jeton

class Grille:

    def __init__(self, g_ligne, g_colonne):
        self.grille = ny.empty((g_ligne, g_colonne), dtype=object)
        self.ligne = g_ligne
        self.colonne = g_colonne

    def coup_valide(self, g_num_colonne):
        return (self.grille[0][g_num_colonne] is None)

    def coup_gagnant(self, couleur):
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
        return (Gestion_jeton.Jeton.nombre_jeton == (self.ligne*self.colonne))

    def vider_grille(self):
        for i in range(self.ligne):
            for j in range(self.colonne):
                if(self.grille[i][j] is not None):
                    self.grille[i][j] = None
        pass
    
    def remplir_grille(self, g_contenu_grille):
        i = 0
        j = 0
        for jeton in g_contenu_grille:
            if(jeton != '0'):
                self.grille[i][j] = Gestion_jeton.Jeton(jeton)
            j += 1
            if(j%self.colonne == 0):
                j = 0
                i += 1
        pass
