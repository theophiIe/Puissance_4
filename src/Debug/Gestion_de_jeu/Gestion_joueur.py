import Jeton
import Grille

class Joueur:
    """
        Classe Joueur cette classe permet créer un joueur.
    """

    def __init__(self, j_commence):
        """
            Constructeur de la classe Joueur permettant de créer un joueur
            en indiquant si le joueur commence ou non la partie.

            Paramètre:
                j_commence : variable de type booléenne qui nous permet de savoir si le 
                             joueur commence la partie ou non.
                             1 commence la partie.
                             0 ne commence pas la partie.
        """
        self.commence = j_commence

    def jouer_coup(self, j_grilles, j_num_colonne):
        """
            Méthode de la classe permettant de placer le jeton
            dans la grille à la colonne souhaitée par le joueur.

            Paramètres:
                j_grilles : matrice de la classe Grille.
                j_num_colonne : variable de type entier positif
                                correspondant à un numéro de colonne
                                de la matrice.

            Cette méthode ne renvoie rien.
        """
        pass

class Ordinateur(Joueur):
    """
        La classe Ordinateur est une classe fille de la classe Joueur.
        
        Cette classe est utilisée pour le joueur contrôlé par l'ordinateur
    """

    def __init__(self, o_commence, o_difficulte):
        """
            Constructeur de la classe Ordinateur. On fait appel au constucteur
            de la classe Joueurs et on définit un niveau de difficulté.

            Paramètres:
                o_commence : variable de type booléenne permettant de savoir
                            si l'ordinateur commence la partie.
                            0 : ne commence pas la partie.
                            1 : commence la partie.
                
                o_difficulte : varible de type entier positif nous permettant de
                                définir le niveau de difficulté de l'ordinateur.
        """
        Joueurs.__init__(o_commence)
        self.difficulte = o_difficulte

    def premier_coup(self, o_grille):
        """
            Cette méthode permet de jouer un jeton au centre de la grille
            si l'ordinateur commence la partie.

            Cette méthode ne renvoie rien.
        """
        pass
