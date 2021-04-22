import numpy as ny
import Puissance_4/src/Gestion_de_Jeu/Gestion_jeton as gj

class Grille:

    def __init__(self, g_ligne, g_colonne):
        self.grille = ny.empty((g_ligne, g_colonne), dtype=object)
        self.ligne = g_ligne
        self.colonne = g_colonne

    def coup_valide(self, g_num_colonne):
        return (self.grille[0][g_num_colonne] is None)

    def coup_gagnant(self, g_num_colonne):
        num_ligne = 5
        for i in range(0,self.ligne):
            if(self.grille[i][g_num_colonne] is not None):
                num_ligne = i
                break
        
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
        return (gj.Jeton.nombre_jeton == (self.ligne*self.colonne))

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
                self.grille[i][j] = gj.Jeton(jeton)
            j += 1
            if(j%self.colonne == 0):
                j = 0
                i += 1
        pass
