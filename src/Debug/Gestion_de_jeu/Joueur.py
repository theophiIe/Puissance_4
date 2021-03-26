import Jeton
import Grille

class Joueur:
    """
        Commentaire sur la classe
    """

    def __init__(self, j_commence):
        """ Commentaire sur le constructeur """
        self.commence = j_commence

    def jouer_coup(self, grilles, j_num_colonne):
        """Commentaire"""
        jeton = Jeton.Jetons(0)
        Jeton.Jetons.incremente_nombre_jeton()
        grilles[0][j_num_colonne] = jeton
        

class Ordinateur(Joueur):
    """
        Commentaire sur la classe (classe fille de Joueur)
    """

    def __init__(self, o_commence, o_difficulte):
        """ Commentaire sur le constructeur """
        Joueur.__init__(o_commence)
        self.difficulte = o_difficulte

    def premier_coup(self):
        """ Commentaire """
        pass


board = Grille.Grilles(7,6)
print(board)

j1 = Joueur(1)
j1.jouer_coup(board, 0)

print(board)